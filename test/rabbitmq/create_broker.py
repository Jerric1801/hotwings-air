import time
import pika

hostname = "localhost" # default hostname
port = 5672            # default port
def create_connection(max_retries=12, retry_interval=5):
    print('amqp_setup:create_connection')
    
    retries = 0
    connection = None
    
    # loop to retry connection upto 12 times with a retry interval of 5 seconds
    while retries < max_retries:
        try:
            print('amqp_setup: Trying connection')
            # connect to the broker and set up a communication channel in the connection
            connection = pika.BlockingConnection(pika.ConnectionParameters
                                (host=hostname, port=port,
                                 heartbeat=3600, blocked_connection_timeout=3600)) # these parameters to prolong the expiration time (in seconds) of the connection
            print("amqp_setup: Connection established successfully")
            break  # Connection successful, exit the loop
        except pika.exceptions.AMQPConnectionError as e:
            print(f"amqp_setup: Failed to connect: {e}")
            retries += 1
            print(f"amqp_setup: Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)

    if connection is None:
        raise Exception("amqp_setup: Unable to establish a connection to RabbitMQ after multiple attempts.")

    return connection

def create_channel(connection, exchange_name, exchange_type):
    print('amqp_setup:create_channel')
    channel = connection.channel()
    # Set up the exchange if the exchange doesn't exist
    print('amqp_setup:create exchange')
    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True) # 'durable' makes the exchange survive broker restarts
    return channel

def construct_queues(channel, build_details):
    for queue_name, values in build_details.items():
        exchange_name = values[0]
        route_key = values[1]
        create_queue(channel, exchange_name, queue_name, route_key)

def create_queue(channel, exchange_name, queue_name, route_key):
    try:
        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=route_key)
    except:
        f"error creating {queue_name}"

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')   
    connection = create_connection()
    channel = create_channel(connection, exchange_name= "payment_topic", exchange_type="topic")
    build_details = {
        "notification_queue": ["payment_topic", "#"],
        "transactions_queue": ["payment_topic", ".trans"],
        "error_queue": ["payment_topic", "*.error"],
        "user": ["payment_topic", "*.user"],
        }
    construct_queues(channel, build_details)


    
    