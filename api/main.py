from fastapi import FastAPI
import pika
import os

app = FastAPI()


@app.get("/")
def root():
    credentials = pika.PlainCredentials(
        os.getenv('RABBITMQ_USER', "user"),
        os.getenv('RABBITMQ_PASS', "pass"))

    parameters = pika.ConnectionParameters(
        os.getenv('RABBITMQ_HOST', "rabbitmq"),
        os.getenv('RABBITMQ_PORT', "5672"),
        os.getenv('RABBITMQ_VHOST', "/"),
        credentials
    )

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    message = "Hello World!"

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    connection.close()
    print(f" [x] Sent '{message}'")
    return {"message": message}
