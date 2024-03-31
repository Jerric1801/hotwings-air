from app.setup import create_connection, create_channel, create_queues

if __name__ == "__main__":
    connection = create_connection()
    channel = create_channel(connection)
    create_queues(channel)