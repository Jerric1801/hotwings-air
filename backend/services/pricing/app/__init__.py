import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_TYPE://USER:PASSWORD@HOST:PORT/DATABASE_NAME'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)  

print(db)

from . import models 
from . import routes 