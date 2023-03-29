import json

key = 'answer'
string_as_json_format = '{"answer": "Hello, User"}'

obj = json.loads(string_as_json_format)

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} нет в объекте")
