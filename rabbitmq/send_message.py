import json

import pika


class PikaClient:
    """Настройка клиент Pika, который будет обрабатывать
    всю связь с RabbitMQ.
    """

    def __init__(self):
        self.publish_queue_name = 'appeal'  # Имя очереди для отправки сообщений
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq",
                                      port=5672,
                                      username="user",
                                      password="password"))
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(
            queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None

    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            body=json.dumps(message)
        )
        self.connection.close()
