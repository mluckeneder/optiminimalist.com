import tornado.web
from coarticles import ArticleParser, ArticleManager
from coarticles import create_manager as manager
from Cheetah.Template import Template
import os
import time

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        arts = manager().get_all_articles()

        self.write(str(Template(file="views/index.tmpl", searchList=[dict(articles=arts)])))

class PostHandler(tornado.web.RequestHandler):
    def get(self, year, month, slug):
        article_key = "/".join((year, month, slug))
        article = manager().get_article(article_key)

        next_article = manager().get_next_article(article_key)
        prev_article = manager().get_prev_article(article_key)

        template_output = Template(file="views/article.tmpl",
                                   searchList=[dict(
                                        article=article,
                                        prev_article=prev_article,
                                        next_article=next_article,
                                        pagetitle=article["title"])])
        self.write(str(template_output))
        # self.write("<br/>".join())

class AtomHandler(tornado.web.RequestHandler):
    def get(self):
        arts = manager().get_all_articles()
        articles = manager().get_all_articles()

        self.write(str(Template(file="views/atom.tmpl", searchList=[dict(modtime=time.gmtime(os.path.getmtime("articles")),
            articles=arts)])))
