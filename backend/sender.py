import pika


class PikaClientSend:

    def main(self, dict_appeal: dict):
        credentials = pika.PlainCredentials(username='user',
                                            password='password')
        parameters = pika.ConnectionParameters("rabbitmq", 5672, "/",
                                               credentials=credentials)
        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        channel.exchange_declare(exchange='test', exchange_type='fanout')  # создаем обменник
        channel.queue_declare(queue='appeal', durable=True)  # создаём очередь
        channel.queue_bind(exchange='test',
                           queue='appeal')  # привязываем обменник к очереди

        channel.basic_publish(exchange='test',
                              routing_key='appeal',
                              body=dict_appeal,
                              properties=pika.BasicProperties(delivery_mode=2))
        connection.close()
