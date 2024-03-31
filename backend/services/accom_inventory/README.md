# File Directory for accom_inventory

- accom_inventory/
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


Hotel Document
{
    "_id": "hotel_456",  // Unique hotel identifier
    "hotel_name": "Airport Plaza Hotel",
    "location_near": "JFK",  // Airport code it's near to
    "address": {
        "street": "123 Airport Road",
        "city": "New York",
        "state": "NY",
        "country": "USA",
        "postal_code": "10010"
    },
    "standard_amenities": ["Wi-Fi", "Air Conditioning", "TV", "Room Service"]
}

Room document
{
    "_id": "room_789",
    "hotel_id": "hotel_456",
    "type": "Standard Double", #can be Family suite too which houses 4 pax
    "max_occupancy": 2,
    "description": "A cozy room perfect for couples or solo travelers. Features one double bed and an en-suite bathroom.",
    "price_per_night": 120,
    "is_available": True // assume queried from hotel side whether this room avail now
}