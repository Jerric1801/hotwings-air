import json
import pika
import socket
import time
from datetime import datetime
from zoneinfo import ZoneInfo

class ActivityLog:
    def __init__(self, correlation_id, microservice, status_code, ip_address, received_time):
        self.correlation_id = correlation_id
        self.microservice = microservice
        self.status_code = status_code
        self.ip_address = ip_address
        self.received_time = received_time

    def to_dict(self):
        return vars(self)

def get_correlation_id():
    return int(time.time() * 1000)

def get_current_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_message_received_time():
    sgt = ZoneInfo('Asia/Singapore')
    received_time_sgt = datetime.now(sgt)
    return received_time_sgt.strftime("%Y-%m-%d %H:%M:%S SGT")

def send_test_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='activity_log')

    correlation_id = get_correlation_id()
    microservice = "Transaction"
    status_code = "500"
    ip_address = get_current_ip_address()
    received_time = get_message_received_time()

    log_entry = ActivityLog(
        correlation_id=correlation_id,
        microservice=microservice,
        status_code=status_code,
        ip_address=ip_address,
        received_time=received_time
    )

    message = json.dumps(log_entry.to_dict())

    channel.basic_publish(exchange='',
                          routing_key='activity_log',
                          body=message)
    
    print(f"Sent: {message}")
    connection.close()

if __name__ == "__main__":
    send_test_message()
