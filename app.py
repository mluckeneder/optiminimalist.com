import tornado.web
import tornado.httpserver
from tornado.options import define, options
from handlers import HomeHandler, PostHandler, AtomHandler
import os
import sys
sys.path.append("./views")


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, type=bool)



class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r'/', HomeHandler),
            (r'/atom\.xml', AtomHandler),
            (r'/([0-9]+)/([0-9]+)/([^\/]+)', PostHandler)
        ]

        settings = {
            'template_path': os.path.join(PROJECT_PATH, 'templates'),
            'static_path': os.path.join(PROJECT_PATH, 'static'),
            'debug': True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    """launch server"""
    tornado.options.parse_command_line()
    print 'Running server on port %s...' % options.port
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    main()
