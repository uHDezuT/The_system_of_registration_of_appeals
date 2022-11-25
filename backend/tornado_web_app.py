import tornado.web
from tornado.ioloop import IOLoop

from rabbitmq.send_message import send_message, receive_message


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
        # if last_name == '':
        #     print('Заполните поле <Фамилия>')
        # elif first_name == '':
        #     print('Заполните поле <Имя>')
        # elif second_name == '':
        #     print('Заполните поле <Отчество>')
        # elif telephone == '':
        #     print('Заполните поле <Телефон>')
        # elif body == '':
        #     print('Напишите текст заявки')
        # else:
        attribute = last_name, first_name, second_name, telephone, body
        send_message(str(attribute))
        receive_message()
        # return print(attribute)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
