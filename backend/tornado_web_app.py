import json
import os

import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

from sender import PikaClientSend


class MainHandler(RequestHandler):
    def get(self):
        self.render("register_form.html")

    def post(self):
        last_name = self.get_argument('last_name')
        first_name = self.get_argument('first_name')
        second_name = self.get_argument('second_name')
        telephone = self.get_argument('telephone')
        body = self.get_argument('body')
        attribute = {'last_name': last_name,
                     'first_name': first_name,
                     'second_name': second_name,
                     'telephone': telephone,
                     'body': body}
        data = json.dumps(attribute)
        PikaClientSend().main(data)
        self.redirect('/successful')



class DoubleHandler(RequestHandler):
    def get(self):
        self.render("end_form.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/successful", DoubleHandler)
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__),
                                          "templates")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    ioloop = tornado.ioloop.IOLoop.instance()

    application = Application()

    application.listen(8000)
    ioloop.start()
