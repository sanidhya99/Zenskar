# Zenskar

This repository is for the Zenskar project.

## Installation

1\. Clone the Git repository: \`\`\`bash 
git clone https://github.com/sanidhya99/Zenskar.git Install the required Python
packages:

bash Copy code pip install pika requests Set up a PostgreSQL database on
your local machine (port 5432) and update the database credentials in
settings.py.

Apply database migrations:

bash Copy code python manage.py makemigrations python manage.py migrate
Usage Start the Django API server:

bash Copy code python manage.py runserver Download and install Ngrok
from its official website.

Unzip Ngrok, open a terminal, and run the following commands:

bash Copy code ngrok config add-authtoken {Your auth token} ngrok http
8000 Ngrok will provide you with a public URL. Use this URL for webhook
configuration in the Stripe developer section.

Create two webhooks in the Stripe developer section:

Webhook 1: Endpoint URL: {Ngrok endpoint}/catalog/customer/ Events:
customer.created Webhook 2: Endpoint URL: {Ngrok
endpoint}/catalog/customer/delete/ Event: customer.deleted In
consumer.py, replace the secret key with the secret key of your Stripe
API.

Docker Setup Install Docker Desktop on your system.

Pull the RabbitMQ Docker image:

bash Copy code docker pull rabbitmq Run RabbitMQ in a Docker container:

bash Copy code docker run -d \--name rabbitmq-container -p 5672:5672 -p
15672:15672 rabbitmq Open localhost:15672 in your web browser to access
the RabbitMQ management dashboard (Username: guest, Password: guest).

Create a queue with the same name as mentioned in consumer.py and
producer.py in your Django app.

In one terminal, run the Django server:

bash Copy code python manage.py runserver In another terminal, navigate
to the directory containing consumer.py and run it as a background
process:

bash Copy code python consumer.py & Integration Testing You are now set
up for integration testing.

License This project is licensed under the \[License Name\] - see the
LICENSE.md file for details.

javascript Copy code

Replace \`{Your auth token}\` with your actual Ngrok authentication
token, and
