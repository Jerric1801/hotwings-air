import requests

response = requests.get("http://localhost:5000/flights")

print(response.content)
