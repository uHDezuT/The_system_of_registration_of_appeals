import ast

import pika
import uvicorn
from fastapi import FastAPI

import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def main():
    credentials = pika.PlainCredentials(username='user',
                                        password='password')
    parameters = pika.ConnectionParameters("rabbitmq", 5672, "/",
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    def callback(ch, method, properties, body):
        body = body.decode("UTF-8")
        body = ast.literal_eval(body)
        last_name = body['last_name']
        first_name = body['first_name']
        second_name = body['second_name']
        telephone = body['telephone']
        body = body['body']
        if last_name or first_name or second_name or telephone or body:
            appeal = models.appeals(last_name=last_name,
                                    first_name=first_name,
                                    second_name=second_name,
                                    telephone=telephone,
                                    body=body)
            db = SessionLocal()
            db.add(appeal)
            db.commit()
            db.refresh(appeal)
            db.close()

    channel.basic_consume(queue='appeal',
                          on_message_callback=callback,
                          auto_ack=True)

    channel.start_consuming()
    uvicorn.run('servisdb.app:app', port=8081)


if __name__ == '__main__':
    main()
