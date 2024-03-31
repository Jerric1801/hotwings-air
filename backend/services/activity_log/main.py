from app import create_app
from app.services import consume_messages
import threading

app = create_app()

if __name__ == "__main__":
    # Run the RabbitMQ consumer in a separate thread
    consumer_thread = threading.Thread(target=consume_messages)
    consumer_thread.start()

    app.run(debug=True, use_reloader=False)
