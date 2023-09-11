import pika
import json

def publish_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()



    channel.basic_publish(
        exchange='',
        routing_key='StripeToAPI',
        body=json.dumps(data)
    )

    connection.close()
