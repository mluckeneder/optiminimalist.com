from flask import Flask, request, make_response
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template

import os
import time

from coarticles import create_manager as manager

app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)
