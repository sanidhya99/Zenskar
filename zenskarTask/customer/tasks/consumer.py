import pika
import json
import requests

def create_stripe_customer(data):
    # Replace with your Stripe API endpoint
    print("entered loop1")
    stripe_api_url = 'https://api.stripe.com/v1/customers'

    # Replace with your Stripe API secret key
    # stripe_api_key = 'sk_test_51NoVtqSFulLe6irUqDTKjGV6hhl3pZZhImw5W7XCZSXap4ILObxuggXXw446q3tboCW7Qw0Ygae7Q67zteAkQAJG004falzVEb'

    print(data)
    headers = {
        'Authorization':'Bearer sk_test_51NoVtqSFulLe6irUqDTKjGV6hhl3pZZhImw5W7XCZSXap4ILObxuggXXw446q3tboCW7Qw0Ygae7Q67zteAkQAJG004falzVEb',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept':'*/*'
    }
    
    response = requests.post(stripe_api_url, data=data, headers=headers)

    if response.status_code == 200:
        print('Stripe customer created successfully.')
    else:
        print(response)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    create_stripe_customer(data)

def consume_queue():
    print("hello entered loop 3")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Don't declare a new queue here, just make sure the existing queue is already created in RabbitMQ

    channel.basic_consume(queue='StripeToAPI', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit, press CTRL+C')

    channel.start_consuming()

if __name__ == '__main__':
    consume_queue()
