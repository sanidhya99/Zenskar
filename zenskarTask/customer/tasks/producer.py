# producer.py

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='customer_updates')

def send_customer_update(customer_id):
    channel.basic_publish(exchange='',
                          routing_key='customer_updates',
                          body=str(customer_id))
    print(f"Sent update for customer {customer_id}")

connection.close()
