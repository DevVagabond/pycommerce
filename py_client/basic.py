import requests

endpoint = "http://localhost:8000/api/"

# GET
get_respose = requests.post(
    endpoint, json={"message": "Hello, World!"}, params={"id": 1})

print(get_respose.text)
