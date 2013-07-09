# -*- coding: utf-8 -*-
from bottle import Bottle, debug, static_file, response, request
from bottle import cheetah_template
from coarticles import ArticleParser, ArticleManager
from coarticles import create_manager as manager
from glob import glob
import os
import time
import config


def setup_cache():
    if config.CACHE:
        if not os.path.isdir("cache_files"):
            os.makedirs("./cache_files")


def cache_file(key, value):
    if config.CACHE:
        setup_cache()


def template_layout(template, *args, **kwargs):

    layout_yield = cheetah_template(template, args, kwargs)
    kwargs_more = dict(kwargs.items() + {"layout_yield": layout_yield}.items())

    if not "pagetitle" in kwargs_more:
        kwargs_more["pagetitle"] = None

    templ = cheetah_template("layout", *args, **kwargs_more)

    return templ

app = Bottle()

@app.route('/mu-e5e1ca4e-dec46de1-f1674442-c0ebb5bb')
def serve_blitz():
	return "42"


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
    articles = manager().get_all_articles()
    return cheetah_template("atom",
                            modtime=time.gmtime(os.path.getmtime("articles")),
                            articles=articles)


@app.route('/static/<filename:path>')
def serve_asset(filename):
    """serves static assets"""
    return static_file(filename, root='./static')


@app.route('/<slug:path>.html')
def article(slug):
    """the page for a single article"""
    article = manager().get_article(slug)


    next_article = manager().get_next_article(slug)
    prev_article = manager().get_prev_article(slug)

    templ = template_layout("article", article=article,
                           prev_article=prev_article,
                           next_article=next_article,
                           pagetitle=article["title"])

    request_path = request.path

    dirname, filename = os.path.dirname(request_path), os.path.basename(request_path)
    if not os.path.isdir("./cache_files%s" % (dirname)):
        os.makedirs("./cache_files%s" % (dirname))
    if not os.path.isfile("./cache_files%s/%s" % (dirname, filename)):
        with open("./cache_files%s/%s" % (dirname, filename), 'w') as f:
            f.write(templ)

    return templ
@app.route('/')
def index():
    """the index page"""
    arts = manager().get_all_articles()
    return template_layout("index", articles=arts)


if __name__ == "__main__":

    debug(True)
    app.run(server='gunicorn',
            host="0.0.0.0",
            port=os.environ.get('PORT', 5000))
