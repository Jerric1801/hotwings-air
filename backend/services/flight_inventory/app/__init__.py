import os
from flask import Flask


def create_app():
    app = Flask(__name__)
#     app.config.from_object(f"app.config.{config_name.capitalize()}Config")

#     db.init_app(app)
    # ... other initializations (blueprints, extensions)

    from .routes import routes_bp  # Example import of routes
    app.register_blueprint(routes_bp)

    return app