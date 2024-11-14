import requests
from datetime import datetime
import os


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_URL = os.environ["SHEETY_URL"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]



NUTRITION_URL = "https://trackapi.nutritionix.com"
GENDER = "male"
WEIGHT = 74
HEIGHT = 189
AGE = 24

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
nutrition_params = {
    "query": input("Please describe your workout:"),
    "gender": GENDER,
    "height_cm": HEIGHT,
    "weight_kg": WEIGHT,
    "age": AGE,
}

response = requests.post(url=f"{NUTRITION_URL}/v2/natural/exercise", json=nutrition_params, headers=nutrition_headers)
workout_result = response.json()
today = datetime.now()
date = today.strftime("%d/%b/%Y")
time = today.strftime("%I:%M %p")

print(workout_result)

sheety_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


for exercise in workout_result["exercises"]:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

data = requests.post(url=SHEETY_URL, json=sheety_params, headers=sheety_headers)
print(data.text)
