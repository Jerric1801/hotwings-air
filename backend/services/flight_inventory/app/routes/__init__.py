# Import necessary modules
from flask import Blueprint

# Create a Blueprint for the routes in this directory
routes_bp = Blueprint('routes', __name__)

# Import specific routes files
from . import seats_api # Assuming flight_search_api.py exists

# Register the blueprints with the main Blueprint
routes_bp.register_blueprint(seats_api.seats_bp)

# Export the main Blueprint (optional, but good practice)
__all__ = ['routes_bp']