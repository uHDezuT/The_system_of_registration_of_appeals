import pika


def send_message(attr: list):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        '127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='appeal')
    channel.basic_publish(exchange='',
                          routing_key='appeal',
                          body=attr)
    connection.close()


def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='appeal')

    body = channel.basic_get('appeal')
    if body:
        print(body)
    else:
        print('No message returned')