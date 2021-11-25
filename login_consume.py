"""This is an example about how to consume a url and get the token with the payloads"""

import requests
import json

url = "https://new-xxxx-qa.xxx.com.co//api/login/"
payload = {'username': 'xxxxx', 'password': 'xxxxxx'}
response = requests.post(url, data=payload)
print(response.text)
