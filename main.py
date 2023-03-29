import requests
from json.decoder import JSONDecodeError

payload = {"name": "User"}

response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
# response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
except JSONDecodeError:
    print("Response is not JSON format")
