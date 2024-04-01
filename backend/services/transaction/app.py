from app import create_app
from app.services import consume_transaction
import threading

app = create_app()

if __name__ == '__main__':
    # Start the RabbitMQ consumer in a separate thread
    consumer_thread = threading.Thread(target=consume_transaction)
    consumer_thread.start()

    # Start the Flask application
    app.run(debug=True)