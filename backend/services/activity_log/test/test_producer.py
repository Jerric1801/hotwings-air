import pika

def send_test_message():
    # Establish a connection with RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue in case it doesn't exist
    channel.queue_declare(queue='activity_log')

    # Send a message to the queue
    message = "Hello, this is a test log message!"
    channel.basic_publish(exchange='',
                          routing_key='activity_log',
                          body=message)

    print(f"Sent: {message}")
    connection.close()

if __name__ == "__main__":
    send_test_message()
