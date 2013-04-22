from glob import glob
import markdown2
import time
from collections import OrderedDict, defaultdict
from coroutine import coroutine, sink, broadcast
import os
import re


class ArticleParser:
    def __init__(self):
        self.articles = OrderedDict()

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
    def slug_enhance(self, target):
        while True:
            article_slug, article = (yield)
            article_slug = "%s/%s" % (time.strftime("%Y/%m", article["date"]),
                                      article_slug)

            target.send((article_slug, article))

    @coroutine
    def article_sink(self, articles):
        try:
            while True:
                article_slug, article = (yield)
                # print((article_slug, article))
        except GeneratorExit:
            print(">>Finished parsing files")

    @coroutine
    def parse_date(self, target):
        print(">>Parsing date")
        while True:
            article_slug, article = (yield)
            converted_date = time.strptime(article["date"], "%Y-%m-%d")
            article["date"] = converted_date

            target.send((article_slug, article))

    @coroutine
    def parse_markdown(self, target):
        print(">>Parsing markdown")
        while True:
            article_slug, article = (yield)
            html = markdown2.markdown(article["content"],
                                      extras=["metadata", "footnotes"])

            article["content"] = html
            article = dict(article, **html.metadata)

            target.send((article_slug, article))

    @coroutine
    def parse_tags(self, target):
        while True:
            article_slug, article = (yield)
            if "tags" in article:
                tags = article["tags"].split(",")
                article["tags"] = [t.strip() for t in tags]

            target.send((article_slug, article))

    @coroutine
    def extract_title(self, target):
        while True:
            article_slug, article = (yield)

            regex = re.compile(".*\# (.+?)\n", re.MULTILINE)
            match = re.search(regex, article["content"])

            if match:
                title = match.group(1).strip()
                print(title)
                article["title"] = title
                article["content"] = re.sub(r'^(\#[^\#]+\n)$',
                                            "", article["content"], count=1)
                # article["content"]\n".join(article["content"].split("\n")[1:])
                article["content"] = re.sub("\x02", "", article["content"])

            target.send((article_slug, article))

    def run_pipeline(self, source, *args):
        sink = broadcast(args)
        slug_enhancer = self.slug_enhance(sink)
        date_parser = self.parse_date(slug_enhancer)
        tag_parser = self.parse_tags(date_parser)
        markdown_parser = self.parse_markdown(tag_parser)
        extract_title = self.extract_title(markdown_parser)
        article_reader = self.article_reader(extract_title)
        self.parse_article_list(source, article_reader)


class ArticleManager(object):
    """docstring for ArticleManager"""
    def __init__(self):
        self.articles = OrderedDict()
        self.articles_index = []
        self.tag_index = defaultdict(OrderedDict)

    def get_article(self, slug):
        return self.articles[slug]

    def get_all_articles(self):
        return self.articles

    @coroutine
    @sink
    def add_article(self, article_slug, article):
        self.articles[article_slug] = article

        self.articles = OrderedDict(sorted(self.articles.items(),
                                    key=lambda k: k[1]["date"],
                                    reverse=True))

    @coroutine
    @sink
    def parse_tags(self, article_slug, article):
        for tag in article["tags"]:
            self.tag_index[tag][article_slug] = article
            # self.tag_index[tag] = OrderedDict(sorted(self.tag_index[tag],
            #                         key=lambda k: k[1]["date"],
            #                         reverse=True))


    @coroutine
    @sink
    def build_index(self, article_slug, article):
        self.articles_index.append(article_slug)

    def build_article_index(self):
        if len(self.articles) != len(self.articles_index):
            self.articles_index = [k for (k, v) in self.articles.items()]

    def get_next_article(self, article_slug):
        """returns the next article of a certain slug"""
        self.build_article_index()

        index = self.articles_index.index(article_slug)

        if index == 0:
            return None
        else:
            key = self.articles_index[index-1]
            return {'id': key, 'article': self.articles[key]}

    def get_prev_article(self, article_slug):
        """returns the previous article of a certain slug"""
        self.build_article_index()

        index = self.articles_index.index(article_slug)

        if index == len(self.articles_index)-1:
            return None
        else:
            key = self.articles_index[index+1]
            return {'id': key, 'article': self.articles[key]}


if __name__ == "__main__":
    parser = ArticleParser()
    manager = ArticleManager()

    parser.run_pipeline(glob("articles/*.md"),
                        manager.add_article(),
                        manager.parse_tags())
    print len(manager.tag_index["python"])