import pika
from pika.adapters.tornado_connection import TornadoConnection


class PikaClient:
    def __init__(self, io_loop):
        self.host = "rabbitmq"
        self.port = 5672
        self.username = "user"
        self.password = "password"
        self.io_loop = io_loop
        self.connected = False
        self.connecting = False
        self.connection = None
        self.channel = None

    def connect(self):
        if self.connecting:
            return
        self.connecting = True
        cred = pika.PlainCredentials(username=self.username,
                                     password=self.password)
        param = pika.ConnectionParameters(self.host, self.port, "/",
                                          credentials=cred)
        self.connection = TornadoConnection(param, custom_ioloop=self.io_loop,
                                            on_open_callback=self.on_connected)
        self.connection.add_on_open_error_callback(self.err)
        self.connection.add_on_close_callback(self.on_closed)

    def err(self, conn):
        print('pika error!')

    def on_connected(self, conn):
        print('pika connected')
        self.connected = True
        self.connection = conn
        self.connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        print(channel)
        channel.exchange_declare(exchange="test", durable=True)  # Switch,
        # persistence
        self.channel = channel

    def on_closed(self, conn, c):
        print('pika close!')
        self.io_loop.stop()
