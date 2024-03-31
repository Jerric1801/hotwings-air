from flask import Flask
from .routes import init_app

def create_app():
    app = Flask(__name__)
    app.secret_key = '123'  # Set a secret key for session management

    init_app(app)  # Initialize your routes

    return app