# -*- coding: utf-8 -*-
from bottle import Bottle, debug, static_file, response
from bottle import cheetah_template
from coarticles import ArticleParser, ArticleManager
from glob import glob
import os
import time


def template_layout(template, *args, **kwargs):
    layout_yield = cheetah_template(template, args, kwargs)
    kwargs_more = dict(kwargs.items() + {"layout_yield": layout_yield}.items())

    if not "pagetitle" in kwargs_more:
        kwargs_more["pagetitle"] = None

    return cheetah_template("layout", *args, **kwargs_more)

app = Bottle()


@app.route('/robots.txt')
def serve_robots():
    """serves the robots.txt file"""
    response.content_type = 'text/plain'
    return open("robots.txt").read()


@app.route('/humans.txt')
def serve_humans():
    """serves the humans.txt file"""
    response.content_type = 'text/plain'
    return open("humans.txt").read()


@app.route('/atom.xml')
def serve_atom():
    articles = loader.get_all_articles()
    return cheetah_template("atom",
                            modtime=time.gmtime(os.path.getmtime("articles")),
                            articles=articles)


@app.route('/static/<filename:path>')
def serve_asset(filename):
    """serves static assets"""
    return static_file(filename, root='./static')


@app.route('/<slug:path>')
def article(slug):
    """the page for a single article"""
    article = loader.get_article(slug)
    next_article = loader.get_next_article(slug)
    prev_article = loader.get_prev_article(slug)

    return template_layout("article", article=article,
                           prev_article=prev_article,
                           next_article=next_article,
                           pagetitle=article["title"])


@app.route('/')
def index():
    """the index page"""
    arts = loader.get_all_articles()
    return template_layout("index", articles=arts)


if __name__ == "__main__":
    parser = ArticleParser()
    manager = ArticleManager()

    env = os.environ.get('ENV', 'development')


    parser.run_pipeline(glob("articles/*.md"),
                        manager.add_article(),
                        manager.parse_tags())

    loader = manager

    debug(True)
    app.run(server='gunicorn',
            host="0.0.0.0",
            port=os.environ.get('PORT', 5000))
