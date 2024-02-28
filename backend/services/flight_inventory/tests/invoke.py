import requests

response = requests.get("http://localhost:5000/flights/flight_123/seats")

print(response.content)
