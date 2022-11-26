import json

string_as_json_format = '{"answer": "Hello, Anton Rodzevich"}'
obj = json.loads(string_as_json_format)
key = 'answer'
if key in obj:
    print(obj[key])
else:
    print(f"Key {key} is not in JSON")