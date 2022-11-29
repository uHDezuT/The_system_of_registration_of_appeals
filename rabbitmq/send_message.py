import pika
import json


def send_message(attr: dict):  # добавление словаря в очередь
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost',
        port=5672))
    channel = connection.channel()
    channel.queue_declare(queue='appeal')
    channel.basic_publish(exchange='',
                          routing_key='appeal',
                          body=json.dumps(attr))
    connection.close()


def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost',
        port=5672))
    channel = connection.channel()

    channel.queue_declare(queue='appeal')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body))

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='appeal')

    channel.start_consuming()
