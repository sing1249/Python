import requests

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

questions = response.json()["results"]

question_data = questions
