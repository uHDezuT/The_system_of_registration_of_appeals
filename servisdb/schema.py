# import db_models
import json
from base64 import b64decode

import pika


class RabbitBody:
    appeal: dict

    def __init__(self, appeal):
        self.appeal = appeal

    def decode(self):
        return json.loads(b64decode(self.appeal))


hostname = "rabbitmq"
port = 5672

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host=hostname, port=port,
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
# Создать канал
channel = connection.channel()
channel.queue_declare(queue='', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    ch.basic_ack(
        delivery_tag=method.delivery_tag)  # Отправить подтверждающее сообщение


# Добавлять параметры, которые не назначают сообщения по порядку, необязательно
# channel.basic_qos(prefetch_count=1)
# Скажите rabbitmq использовать обратный вызов для получения информации
channel.basic_consume(callback, queue='',
                      no_ack=False)  # no_ack, чтобы указать, следует ли отправлять подтверждение, по умолчанию False, открытое состояние

# Начните получать информацию и войдите в состояние блокировки, обратный вызов будет вызван для обработки, когда в очереди есть информация, нажмите Ctrl + C для выхода
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
