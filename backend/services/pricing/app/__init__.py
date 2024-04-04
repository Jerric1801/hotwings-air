import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .services import consume_amqp_messages
from .amqp_setup import create_channel
from .amqp_connection import create_connection
from threading import Thread


app = Flask(__name__)
CORS(app)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:strong_password@sql_db:3306/prices' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
try:
    db = SQLAlchemy(app)  

    with app.app_context():
        db.create_all()

    def start_amqp_thread():
        connection = create_connection()
        channel = create_channel(connection)
        consume_amqp_messages(channel) 

    amqp_thread = Thread(target=start_amqp_thread)
    amqp_thread.start()
except:
    print("failed to connect")



from . import models 
from . import routes 
from . import services
from . import amqp_connection
from . import amqp_setup

