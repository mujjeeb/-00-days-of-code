import requests
from datetime import datetime
import os



GENDER = ['Your gender']
WEIGHT_KG = ['Your weight']
HEIGHT_CM = ['Your height']
AGE = ['Your age']

APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
API_KEY = os.environ.get('NUTRITIONIX_APP_KEY')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_text = input("Tell me which exercises you did: ")
post_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=post_endpoint, json=post_body, headers=headers)
result = response.json()
print(result)

today = datetime.strftime(datetime.now(), '%d/%m/%Y')
time_now = datetime.strftime(datetime.now(), '%H:%M:%S')
print(today)
print(time_now)

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

sheety_headers = {"Authorization": os.environ.get("SHEETY_BEARER_AUTH")}

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

print(sheety_response.text)

sheety_response = requests.get(url=sheety_endpoint,json=sheet_inputs, 
    headers=sheety_headers)
print(sheety_response.text)






