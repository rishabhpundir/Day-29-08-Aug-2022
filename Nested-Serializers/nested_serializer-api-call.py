import json
from urllib import request
import requests

response = requests.get(url='http://127.0.0.1:8000/singers/')
data = response.json()
print(data)