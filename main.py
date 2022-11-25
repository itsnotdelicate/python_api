import requests

payload = {"name": "Anton Rodzevich"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response)
print(response.text)