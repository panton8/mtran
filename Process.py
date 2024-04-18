import requests

url = "https://api.jdoodle.com/v1/execute"
api_key = "50251df3dcc83cc57d797c5cd6781213"
lang = "pascal"


def process(file_name):
    with open(file_name) as file:
        code = file.read()

    payload = {
        "clientId": "50251df3dcc83cc57d797c5cd6781213",
        "clientSecret": "f1b5d5f71de751a97e9ed5bc1063db1fd9c87eb1f11d703bc902f04f65d03c34",
        "script": code,
        "language": lang
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Status code: {response.status_code}")
        print("Error!")
