# File Directory for flight_inventory

- flight_inventory/
- ├── app/
- │   ├── __init__.py   # Application initialization
- │   ├── config.py     # Application configurations
- │   ├── models.py     # Database models 
- │   ├── routes.py     # API endpoints/views
- │   ├── services.py   # Business logic
- │   └── utils.py      # Helper functions 
- ├── requirements.txt  # Python dependencies
- ├── run.py            # Script to start the Flask app
- ├── config.py         # Environment-specific configuration
- ├── Dockerfile        # For containerization
- └── README.md         # Project documentation

Flight Document
{
    "_id": "flight_123",  // Unique flight identifier
    "flight_number": "AC105",
    "departure": "2024-03-03T09:00:00Z",
    "arrival": "2024-03-03T15:30:00Z",
    "origin": "SIN",
    "destination": "JFK",
    "aircraft": "Boeing 777-300ER",
    "seating_plan": {  // Reference to seating plan
        "_id": "seating_ac105_20240303" 
    }
}

Seating Plan Document
{
    "_id": "seating_ac105_20240303", 
    "aircraft_type": "Boeing 777-300ER",
    "date": "2024-03-03",
    "layout": [
        { "row": 1,  "seats": ["1A", "1B", "1C", "1D"] },
        { "row": 2,  "seats": ["2A", "2B", "2C", "2D"] },
        // ... more rows
    ],
    "availability": {
        "1A": "available", 
        "1B": "booked",
        // ... availability for all seats
    }
}