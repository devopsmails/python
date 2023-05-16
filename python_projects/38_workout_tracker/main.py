import requests
from datetime import datetime

GENDER = " male"
WEIGHT = 74
HEIGHT = 182
AGE = 28

APP_ID = "c75458fa"
API_KEY = "419389495b8ec29f6a285d6cd2632504"


excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/7c6b533b996fa94d8d028d1739781775/sureshWorkouts/workouts"

excercise_text = input("Tell me What Excercise you did today? : ")


headers = {
    "x-app-id" : APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query" : excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(excercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today = datetime.now().strftime("%d%m%y")
print(today)

now_time = datetime.now().strftime("X")
print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
print(sheet_response.text)
