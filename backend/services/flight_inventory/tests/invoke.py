import requests
import json

response = requests.get("http://localhost:5000/flight/HWA 300")

print(response.content)
