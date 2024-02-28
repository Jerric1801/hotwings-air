import os
from flask import Flask


def create_app():
    app = Flask(__name__)
#     app.config.from_object(f"app.config.{config_name.capitalize()}Config")

#     db.init_app(app)
    # ... other initializations (blueprints, extensions)

#     from .routes import search_api  # Example import of routes
#     app.register_blueprint(search_api)

    return app