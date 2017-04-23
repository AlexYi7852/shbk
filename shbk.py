#coding: utf8
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
define("port", default=5002, help="run on the given port", type=int)

from handler.hot import HotHandler, LoginHandler, ApiLoginHandler,RegisterHandler, ApiRegisterHandler

settings = {
    'debug' : True,
    'template_path' : os.path.join(os.path.dirname(__file__),"front"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static")
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r"/", HotHandler),
            (r"/login", LoginHandler),
            (r"/api/login",ApiLoginHandler),
            (r"/register", RegisterHandler),
            (r"/api/register", ApiRegisterHandler)
        ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()