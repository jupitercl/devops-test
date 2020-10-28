from fastapi import FastAPI
import pika

app = FastAPI()


@app.get("/")
def root():
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

    message = "Hello World!"

    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
    connection.close()
    print(f" [x] Sent '{message}'")
    return {"message": message}
