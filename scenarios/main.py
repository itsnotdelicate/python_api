import requests

payload = {"name": "Anton Rodzevich"}
key = "answer1"

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response_text = response.json()

if key in parsed_response_text:
    print(parsed_response_text[key])
else:
    print(f"Key '{key}' is not in JSON")
