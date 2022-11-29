import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
for response_detailed in response.history:
    print(response_detailed.url)
    print(response_detailed.status_code)