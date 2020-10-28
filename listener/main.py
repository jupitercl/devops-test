import time

import pika

import db
from models import Mensaje

print("creando las tablas")
db.Base.metadata.create_all(db.engine)

credentials = pika.PlainCredentials("user", "pass")

parameters = pika.ConnectionParameters(
    "rabbitmq",
    "5672",
    '/',
    credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("ejecutando tarea pesada")
    time.sleep(1)
    print("tarea lista")

    msg = Mensaje(str(body, 'utf-8'))
    db.session.add(msg)
    db.session.commit()


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
