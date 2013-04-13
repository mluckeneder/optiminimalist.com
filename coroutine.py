def coroutine(func):
    """turns a function into a coroutine"""
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start


def article_filter(func):
    def start(target, *args, **kwargs):
        while True:
            article_slug, article = (yield)
            article_slug, article = func(article_slug, article)
            target.send((article_slug, article))
    return start


def sink(func):
    def start(self, *args, **kwargs):
        try:
            while True:
                article_slug, article = (yield)
                func(self, article_slug, article, *args, **kwargs)
        except GeneratorExit:
            print("Done!")
    return start


@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
