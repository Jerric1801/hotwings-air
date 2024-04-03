from app import app
# from app.services import consume_messages
# import threading

if __name__ == "__main__":
    # Run the RabbitMQ consumer in a separate thread
    # consumer_thread = threading.Thread(target=consume_messages)
    # consumer_thread.start()

    app.run(debug=True, host='0.0.0.0', port = '5020')