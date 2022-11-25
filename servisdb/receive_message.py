import pika


def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='appeal')
    print(channel.basic_consume(queue='appeal',
                                no_ack=True))

    channel.start_consuming()

receive_message()