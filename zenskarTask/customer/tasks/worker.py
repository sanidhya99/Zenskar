# worker.py

import pika
import stripe
from customer.models import *

stripe.api_key = 'sk_test_51NoVtqSFulLe6irUqDTKjGV6hhl3pZZhImw5W7XCZSXap4ILObxuggXXw446q3tboCW7Qw0Ygae7Q67zteAkQAJG004falzVEb'

def callback(ch, method, properties, body):
    customer_id = int(body)
    # Fetch the customer from your database and sync to Stripe here
    # Example:
    customer = Customer.objects.get(id=customer_id)
    stripe.Customer.modify(customer.stripe_id, name=customer.name, email=customer.email)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='customer_updates')

channel.basic_consume(queue='customer_updates', on_message_callback=callback, auto_ack=True)

print('Waiting for updates. To exit press CTRL+C')
channel.start_consuming()
