# Zenskar

To integrate stripe test account with local relational database through Django API server and RabbitMQ.

## Installation

1. Clone the Git repository:
   ```git clone https://github.com/sanidhya99/Zenskar.git```
3. Install required Python packages:
   ```pip install pika requests```
4. Set up a PostgreSQL database on your local machine (port 5432) and update the database credentials in settings.py.
5. Apply database migrations:
   ```python manage.py makemigrations```
   ```python manage.py migrate```

## Usage
1. Start the Django API server:
    ```python manage.py runserver```
2. Download and install Ngrok from its official website.
3. Unzip Ngrok, open a terminal, and run the following commands:
   ```
   ngrok config add-authtoken {Your auth token}
   ngrok http 8000
   ```
4. Ngrok will provide you with a public URL. Use this URL for webhook configuration in the Stripe developer section.
5. Create two webhooks in the Stripe developer section:
   - **Webhook 1:**
     - Endpoint URL: ```{Ngrok endpoint}/catalog/customer/```
     - Events: `customer.created`

   - **Webhook 2:**
     - Endpoint URL: ```{Ngrok endpoint}/catalog/customer/delete/```
     - Event: `customer.deleted`
6.In consumer.py, replace the secret key with the secret key of your Stripe API.
## Docker Setup
1. Install Docker Desktop on your system.
2. Pull the RabbitMQ Docker image:
   ```docker pull rabbitmq```
3. Run RabbitMQ in a Docker container:
   ```docker run -d --name rabbitmq-container -p 5672:5672 -p 15672:15672 rabbitmq```
4. Open localhost:15672 in your web browser to access the RabbitMQ management dashboard (Username: guest, Password: guest).
5. Create a queue with the same name as mentioned in consumer.py and producer.py in your Django app.
6. In one terminal, run the Django server:
   ```python manage.py runserver```
7. In another terminal, navigate to the directory containing consumer.py and run it as a background process:
   ```python consumer.py```
## Integration Testing
   You are now set up for integration testing.
            

     
   
            
