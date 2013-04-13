from glob import glob
# import markdown2
# import time
# from collections import OrderedDict, defaultdict
from coroutine import coroutine
import os
import re

class ArticleParser:
    def parse_article_list(self, files, target):
        for f in files:
            target.send(f)
        target.close()

    @coroutine
    def article_reader(self, target):
        print(">>Reading files")
        while True:
            file_name = (yield)
            with open(file_name) as f:
                article_id = os.path.basename(file_name)

                regex = r'(\d{4}\-\d{2}\-\d{2})\-(.+)\.md'
                match = re.match(regex, article_id)

                if match:
                    article_date, article_slug = match.group(1), match.group(2)
                    content = f.read()
                    article = {'date': article_date,
                               'content': content}
                    target.send((article_slug, article))

    @coroutine
    def printer(self):
        try:
            while True:
                article_slug, article = (yield)
                print(article_slug)
        except GeneratorExit:
            print(">>Finished parsing files")


    @coroutine
    def parse_date(self, target):
        print(">>Parsing date")
        while True:
            article_slug, article = (yield)
            target.send(article["date"])


    # @coroutine
    # def parse_markdown(self, target):
    #     while True:
    #         content = (yield)


    def run_pipeline(self, files):
        printer = self.printer()
        date_parser = self.parse_date(printer)
        article_reader = self.article_reader(date_parser)
        self.parse_article_list(files, article_reader)


if __name__ == "__main__":
    parser = ArticleParser()
    parser.run_pipeline(glob("articles/*.md"))


# class Loader:
#     """loads articles"""
#     def __init__(self, path="./articles/*.md"):
#         self.path = path
#         self.articles = self.compile_article_list(raw_articles)
#         self.articles_index = self.compile_article_index(self.articles)
        

#     def compile_article_list_index(self, articles):
#         return {article["raw_date"]: article
#                 for id, article in articles.items()}

#     def get_all_articles(self):
#         """get all articles"""
#         return self.articles

#     def get_article(self, article_slug):
#         """get an article with a certain slug"""
#         return self.articles[article_slug]

#     def get_next_article(self, article_slug):
#         """returns the next article of a certain slug"""
#         index = self.articles_index.index(article_slug)

#         if index == 0:
#             return None
#         else:
#             key = self.articles_index[index-1]
#             return self.articles[key]

#     def get_prev_article(self, article_slug):
#         """returns the previous article of a certain slug"""
#         index = self.articles_index.index(article_slug)

#         if index == len(self.articles_index)-1:
#             return None
#         else:
#             key = self.articles_index[index+1]
#             return self.articles[key]

#     def load_articles(self, article_location):
#         """loads articles from directory"""
#         article_files = glob.glob(article_location)
#         articles = {}

#         for article in article_files:
#             with open(article) as content:
#                 fname = article.split("/")[-1].split(".")[0]
#                 articles[fname] = content.read()

#         return articles

#     def compile_article(self, id, article):
#         """compiles an article from raw input into a useable format"""
#         html = markdown2.markdown(article, extras=["metadata", "footnotes"])
#         metadata = html.metadata
#         metadata["raw_date"] = metadata["date"]

#         converted_date = time.strptime(metadata["date"], "%d/%m/%Y")
#         metadata["date"] = converted_date
#         metadata["text"] = html
#         metadata["id"] = id
#         return metadata

#     def compile_article_list(self, articles):
#         """compiles the above list into ready to publish format"""
#         articles = {id: self.compile_article(id, article)
#                     for id, article in articles.items()}

#         # sort articles
#         sorted_articles = OrderedDict(sorted(articles.items(),
#                                       key=lambda k: k[1]["date"], reverse=True))
#         return sorted_articles

#     def compile_article_index(self, articles):
#         return [k for (k, v) in articles.items()]
