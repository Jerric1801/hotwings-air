# File Directory for accom_inventory

- accom_inventory/
- ├── app/
- │   ├── __init__.py   # Application initialization
- │   ├── config.py     # Application configurations
- │   ├── models.py     # Database models 
- │   ├── routes.py     # API endpoints/views
- │   ├── schema.py     # Schema for GraphQL
- │   └── utils.py      # Helper functions 
- ├── requirements.txt  # Python dependencies
- ├── run.py            # Script to start the Flask app
- ├── config.py         # Environment-specific configuration
- ├── Dockerfile        # For containerization
- └── README.md         # Project documentation


Hotel Document
{
  "_id": {
    "$oid": "660a0b2eae6e48d60c025b66"
  },
  "hotel_name": "Gateway Inn JFK",
  "location_near": "JFK",
  "address": {
    "street": "123 JFK Blvd",
    "city": "New York",
    "state": "NY",
    "zip": "11101"
  },
  "rooms": [
    {
      "type": "Standard Double",
      "max_occupancy": 2,
      "description": "A comfortable room for couples or solo travelers.",
      "price_per_night": 120,
      "is_available": true,
      "_id": {
        "$oid": "660a0b2eae6e48d60c025b4c"
      }
    },
    {
      "type": "Family Suite",
      "max_occupancy": 4,
      "description": "Spacious room perfect for families, with two queen beds.",
      "price_per_night": 180,
      "is_available": true,
      "_id": {
        "$oid": "660a0b2eae6e48d60c025b4d"
      }
    },
    {
      "type": "Executive Suite",
      "max_occupancy": 2,
      "description": "Luxury accommodation with a king-size bed and office space.",
      "price_per_night": 220,
      "is_available": true,
      "_id": {
        "$oid": "660a0b2eae6e48d60c025b4e"
      }
    },
    {
      "type": "Deluxe Double",
      "max_occupancy": 2,
      "description": "Double room with extra comfort amenities.",
      "price_per_night": 150,
      "is_available": true,
      "_id": {
        "$oid": "660a0b2eae6e48d60c025b4f"
      }
    },
    {
      "type": "Quadruple Room",
      "max_occupancy": 4,
      "description": "Ideal for groups, featuring two double beds.",
      "price_per_night": 200,
      "is_available": true,
      "_id": {
        "$oid": "660a0b2eae6e48d60c025b50"
      }
    }
  ]
}
