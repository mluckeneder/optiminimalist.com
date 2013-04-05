import glob
import markdown2
import time


def load(article_location="./articles/*.md"):
    """loads articles from directory"""
    article_files = glob.glob(article_location)
    articles = {}

    for article in article_files:
        with open(article) as content:
            fname = article.split("/")[-1].split(".")[0]
            articles[fname] = content.read()

    return articles


def compile_article(article):
    """compiles an article from raw input into a useable format"""
    html = markdown2.markdown(article, extras=["metadata"])
    metadata = html.metadata

    converted_date = time.strptime(metadata["date"], "%d/%m/%Y")
    metadata["date"] = converted_date
    metadata["text"] = str(html)
    return metadata


def compile_article_list(articles):
    """compiles the above list into ready to publish format"""
    return {id: compile_article(article) for id, article in articles.items()}


if __name__ == "__main__":
    articles = compile_article_list(load())

    print(articles)
