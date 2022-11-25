import requests

payload = {"login": "secret_login", "password": "secret_pass1"}
response_cookie = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response_cookie.cookies.get("auth_cookie")

cookie_auth = {}
if cookie_value is not None:
    cookie_auth.update({"auth_cookie": cookie_value})
else:
    print("Cookie is None")

response_auth = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie_auth)
print(response_auth.text)
print(response_auth.status_code)