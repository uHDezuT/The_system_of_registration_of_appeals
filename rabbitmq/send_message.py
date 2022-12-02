import json

import pika


def receive_message():  # Пока извлечение из очереди с ошибкой!!!!!!!!!
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost',
        port=5672))
    channel = connection.channel()
    channel.queue_declare(queue='appeal')

    def callback(ch, method, properties, body):
        print(json.loads(body))

    channel.basic_consume(callback,
                          queue='appeal')
    channel.start_consuming()


class PikaClient:
    """Настройка клиент Pika, который будет обрабатывать
    всю связь с RabbitMQ.
    """

    def __init__(self, process_callable):
        self.publish_queue_name = 'appeal'  # Имя очереди для отправки сообщений
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost',
                                      port=5672))
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(
            queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_callable = process_callable  # вызываемый обратный вызов,

        # который будет обрабатывать фактическую бизнес-логику
        # для обработки входящего сообщения

    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            body=json.dumps(message)
        )
        self.connection.close()
