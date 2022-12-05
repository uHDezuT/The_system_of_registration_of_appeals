import json
import pika
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
from sender import PikaClient


class MainHandler(RequestHandler):
    def get(self):
        self.render("frontend/register_form.html")

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
        # if not self.application.pika.connecting:
        self.application.pika.connect()
        self.application.pika.channel.basic_publish(exchange="test",
                                                    queue='appeal',
                                                    body=data,
                                                    properties=
                                                    pika.BasicProperties(
                                                        delivery_mode=2))

        print("Push successfully.")
        self.render("frontend/register_form.html")



def make_app():
    handlers = [
        (r"/", MainHandler)
    ]
    app = tornado.web.Application(handlers=handlers, debug=True)
    return app


if __name__ == '__main__':
    ioloop = tornado.ioloop.IOLoop.instance()

    application = make_app()
    application.pika = PikaClient(ioloop)
    application.pika.connect()

    application.listen(8000)
    ioloop.start()
