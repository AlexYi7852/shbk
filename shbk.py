#coding: utf8

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
define("port", default=5010, help="run on the given port", type=int)

from handler.index import HotHandler, LoginHandler, ApiLoginHandler, RegisterHandler, ApiRegisterHandler
from handler.article import SubmissionHandler, ApiSubmissionHandler, CommentHandler, ApiCommentHandler

settings = {
    'debug' : True,
    'template_path': os.path.join(os.path.dirname(__file__), "front"),
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", HotHandler),
            (r"/login", LoginHandler),
            (r"/api/login",ApiLoginHandler),
            (r"/register", RegisterHandler),
            (r"/api/register", ApiRegisterHandler),
            (r"/submission", SubmissionHandler),
            (r"/api/submission", ApiSubmissionHandler),
            (r"/comment", CommentHandler),
            (r"/api/comment", ApiCommentHandler)
        ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()