import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from app.services import consume_amqp_messages
from app.amqp_connection import create_connection
from app.amqp_setup import create_channel
import threading

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

try: 

    client = MongoClient('mongodb://root:example@host.docker.internal:27017/accom_inventory')
    db = client['accom_inventory'] 

    connection  = create_connection()

    channel = create_channel(connection)

    consume_amqp_messages(channel)
    
    # consumer_thread = threading.Thread(target=consume_transaction)
    # consumer_thread.start()

    # connect(db='accom_inventory', host='localhost', port=27017) 

except:
    print("Failed to connect to mongodb") 


from . import models 
from . import routes 
from . import schema