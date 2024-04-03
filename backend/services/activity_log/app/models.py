class ActivityLog:
    def __init__(self, correlation_id, microservice, status_code, ip_address, received_time):
        self.correlation_id = correlation_id
        self.microservice = microservice
        self.status_code = status_code
        self.ip_address = ip_address
        self.received_time = received_time
