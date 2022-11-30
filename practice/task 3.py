import requests

get_param = {"method": "GET"}

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Response 1 (method not provided) result: {response1.text}")

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Response 2 (unsupported method) result: {response2.status_code}")

response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=get_param)
print(f"Response 3 (correct method provided) result: {response3.text}")

parameters = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for obj in parameters:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=obj)
    print(f"""Trying GET request with "{obj}": {response.text}""")