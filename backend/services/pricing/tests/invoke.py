import requests
import json

response = requests.get("http://127.0.0.1:5003/pricing/HWA552")
print(response.content)