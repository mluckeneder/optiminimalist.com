import glob
import markdown2
import time
from collections import OrderedDict, defaultdict


class Loader:
    """loads articles"""
    def __init__(self, path="./articles/*.md"):
        self.path = path
        raw_articles = self.load_articles(path)
        self.articles = self.compile_article_list(raw_articles)
        self.article_index = self.indexify_article_list_index(self.compile_article_list_index(
            self.articles))

    def compile_article_list_index(self, articles):
        return {article["raw_date"]: article
                for id, article in articles.items()}

    def get_all_articles(self):
        """get all articles"""
        return self.articles

    def get_article(self, article_id):
        """get an article with a certain id"""
        return self.articles[article_id]

    def load_articles(self, article_location):
        """loads articles from directory"""
        article_files = glob.glob(article_location)
        articles = {}

        for article in article_files:
            with open(article) as content:
                fname = article.split("/")[-1].split(".")[0]
                articles[fname] = content.read()

        return articles

    def indexify_article_list_index(self, articles, index=2):
        """parses dates from article_index"""
        if index < 0:
            return {a["id"]: a for _, a in articles.items()}

        new_articles = defaultdict(dict)
        temp_articles = defaultdict(dict)

        for key, article in articles.items():
            key_component = key.split("/")[index]
            temp_articles[key_component][key] = article

        for key, article in temp_articles.items():
            temp_articles[key] = self.indexify_article_list_index(
                article, index-1)

        return dict(temp_articles)

    def compile_article(self, id, article):
        """compiles an article from raw input into a useable format"""
        html = markdown2.markdown(article, extras=["metadata"])
        metadata = html.metadata
        metadata["raw_date"] = metadata["date"]

        converted_date = time.strptime(metadata["date"], "%d/%m/%Y")
        metadata["date"] = converted_date
        metadata["text"] = html
        metadata["id"] = id
        return metadata

    def compile_article_list(self, articles):
        """compiles the above list into ready to publish format"""
        articles = {id: self.compile_article(id, article)
                    for id, article in articles.items()}

        # sort articles
        return OrderedDict(sorted(articles.items(),
                                  key=lambda k: k[1]["date"], reverse=True))

if __name__ == "__main__":
    from pprint import pprint
    l = Loader()
    pprint(dict(l.indexify_article_list_index(l.article_index)))
