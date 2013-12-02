from flask import Flask, request, make_response
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template

import os
import time

from coarticles import create_manager as manager

app = Flask(__name__, static_folder='static')
mako = MakoTemplates(app)


@app.route('/')
def index():
    arts = manager().get_all_articles()
    return render_template('index.html', articles=arts.items())

@app.route('/atom.xml')
def atom():
    arts = manager().get_all_articles()

    response = make_response(
        render_template(
        'atom.mako',
        modtime=time.gmtime(os.path.getmtime("articles")),
        articles=arts.items()
        )
    )
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route('/<int:year>/<int:month>/<slug>')
def show_post(year, month, slug):
    article_key = "/".join(
        (
            "%02d" % year,
            "%02d" % month,
            slug
        )
    )
    article = manager().get_article(article_key)

    next_article = manager().get_next_article(article_key)
    prev_article = manager().get_prev_article(article_key)

    return render_template(
        'article.mako',
        article=article,
        prev_article=prev_article,
        next_article=next_article,
        pagetitle=article["title"]
    )

if __name__ == '__main__':
    app.run(debug=True)
