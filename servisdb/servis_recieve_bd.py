import asyncio
import json
import os

import pika
from aiormq.abc import DeliveredMessage
from databases import Database
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import create_engine, MetaData
#
# from schema import RabbitBody
#
# exchange_name = os.environ.get("EXCHANGE_NAME")
# rabbitmq_host = os.environ.get("RABBITMQ_HOST")
# rabbitmq_user = os.environ.get("RABBITMQ_USER")
# rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")
#
# postgres_host = os.environ.get("POSTGRES_HOST")
# postgres_port = os.environ.get("POSTGRES_PORT")
# postgres_database = os.environ.get("POSTGRES_DB")
# postgres_user = os.environ.get("POSTGRES_USER")
# postgres_password = os.environ.get("POSTGRES_PASSWORD")
#
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(postgres_user,
#                                                     postgres_password,
#                                                     postgres_host,
#                                                     postgres_port,
#                                                     postgres_database)
#
# engine = create_engine(DATABASE_URL)
# database = Database(DATABASE_URL)
# metadata = MetaData()
#
# appeals = Table(
#     'appeals', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('last_name', String),
#     Column('first_name', String),
#     Column('second_name', String),
#     Column('telephone', String),
#     Column('body', String)
# )
#
#
# async def insert_appeals(message: DeliveredMessage):
#     response = RabbitBody.decode(message.body)
#     query = appeals.insert().values(last_name=response.appeal['last_name'],
#                                     first_name=response.appeal['first_name'],
#                                     second_name=response.appeal['second_name'],
#                                     telephone=response.appeal['telephone'],
#                                     body=response.appeal['body'])
#     await database.connect()
#     await database.execute(query=query)
#     await database.disconnect()
#
#     await message.channel.basic_ack(
#         message.delivery.delivery_tag
#     )


def callback(ch, method, properties, body):
    message = json.loads(body)
    return print(message)


def consume():
    credentials = pika.PlainCredentials(username='user',
                                        password='password')
    parameters = pika.ConnectionParameters("rabbitmq", 5672, "/",
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.basic_qos(prefetch_count=1)  # обработка 1 сообщения в единицу времени

    channel.exchange_declare(exchange='test', exchange_type='fanout')

    channel.queue_declare(queue='appeal',
                                durable=True,
                                auto_delete=True)

    channel.basic_consume(routing_key='appeal',
                          consumer_callback=callback,
                          auto_ack=True)
    channel.start_consuming()
    # await channel.basic_consume(declare.queue, insert_appeals)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(consume())
    # loop.run_forever()
    consume()