# Zenskar

To integrate stripe test account with local relational database through Django API server and RabbitMQ.

## Installation

1. Clone the Git repository:
      `git clone https://github.com/sanidhya99/Zenskar.git`
2. Install required Python packages:
   `pip install pika requests`
3. Set up a PostgreSQL database on your local machine (port 5432) and update the database credentials in settings.py.
4. Apply database migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`

## Usage
1. Start the Django API server:
    `python manage.py runserver`
2. Download and install Ngrok from its official website.
3. Unzip Ngrok, open a terminal, and run the following commands:
   <pre>
   ```bash
    ngrok config add-authtoken {Your auth token}
    ngrok http 8000

   ```
   </pre>   
   
            
