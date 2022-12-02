import tornado.web
from tornado.ioloop import IOLoop

from rabbitmq.send_message import PikaClient


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("../frontend/register_form.html")

    def post(self) -> list[str]:
        self.render("../frontend/register_form.html")
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
        PikaClient().send_message(attribute)
        # return print(attribute)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
