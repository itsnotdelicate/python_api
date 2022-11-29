import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(f"The URL at the end of redirects is '{response.url}'")
counter = 0
for redirect in response.history:
    counter += 1
print(f"The amount of redirects: {counter}")