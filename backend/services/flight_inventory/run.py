import os
from app import create_app  # Assuming your Flask app creation is in a 'create_app' function
# from app.models import db  # Assuming you're using an ORM like SQLAlchemy
# from app.services import message_producer  # Example, if you have one

# Environment based configuration (adjust as needed)
config_name = os.getenv("FLASK_ENV", "development")
app = create_app()

# # Initialize Database (assuming SQLAlchemy)
# db.init_app(app)
#
# # RabbitMQ Connection Setup (if applicable)
# if 'RABBITMQ_HOST' in os.environ:
#     # Initialize the message producer based on RabbitMQ environment variables
#     message_producer.init_connection()

if __name__ == '__main__':
    app.run()