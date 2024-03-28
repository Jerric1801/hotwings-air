from flask import Flask
from .routes import error_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(error_blueprint, url_prefix='/error')
    return app