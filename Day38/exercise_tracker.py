import requests
from dotenv import load_dotenv
from pathlib import Path
import os
from datetime import datetime

load_dotenv(dotenv_path=Path("./Day38/.env"))

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

workout = input("Tell me what exercises you did: ")

exercise_params = {
    'query': workout
}

header = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

nutritionix_response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_params, headers=header)
data = nutritionix_response.json()
sheety_header = {
        'Content_Type': 'application/json',
        'Authorization': f"Bearer {os.environ.get('BEARER_TOKEN')}" # Optional. Depends on the authorization you chose.
    }
sheety_url = os.environ.get("SHEETY_URL")
for row in data['exercises']:
    date = datetime.now().strftime('%m/%d/%Y')
    time = datetime.now().strftime('%H:%M:%S')
    add_row_body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': row['user_input'].title(),
            'duration': row['duration_min'],
            'calories': row['nf_calories']
        }
    }
    sheety_response = requests.post(sheety_url, json=add_row_body, headers=sheety_header)
    print(sheety_response.text)