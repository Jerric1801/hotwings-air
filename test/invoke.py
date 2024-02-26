import requests

response = requests.post("http://localhost:5001/payment")
print(response.content)