from flask import Flask
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template

from coarticles import create_manager as manager

app = Flask(__name__)
mako = MakoTemplates(app)


@app.route('/')
def index():
    arts = manager().get_all_articles()
    return render_template('index.html', articles=arts.items())

if __name__ == '__main__':
    app.run(debug=True)
