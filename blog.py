# -*- coding: utf-8 -*-
from bottle import route, run, debug
#from bottle import cheetah_view as view
from bottle import cheetah_template as template
import articles
import os


@route('/')
def index():
    """the index page"""
    arts = articles.load()
    return template("index", articles=articles.compile_article_list(arts))


@route('/contact')
def contact():
    """contact me page"""
    return template("this is cool")

debug(True)
run(server='gunicorn', port=os.environ.get('PORT', 5000), reloader=True)
