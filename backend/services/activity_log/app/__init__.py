from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = '123'  # Set a secret key for session management

CORS(app)

from . import routes