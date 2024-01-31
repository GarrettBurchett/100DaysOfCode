import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./Day35/.env')
load_dotenv(dotenv_path=dotenv_path)

weather_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT")
auth_token = os.environ.get("AUTH_TOKEN")

geolocate_params = {
    'q': 'Houston, TX, USA', # city_name, state_code, country_code
    'appid': weather_api_key
}

geo_response = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=geolocate_params)
geo_response.raise_for_status()
latitude = geo_response.json()[0]['lat']
longitude = geo_response.json()[0]['lon']

forecast_params = {
    'lat': latitude,
    'lon': longitude,
    'appid': weather_api_key,
    'units': 'imperial',
    'cnt': 4
}

forecast_response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=forecast_params)
forecast_response.raise_for_status()
weather_data = forecast_response.json()

for item in weather_data['list']:
    if item['weather'][0]['id'] < 700:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_=os.environ.get("TWILIO_PHONE"),
        body="It's going to rain today. Remember to bring an ☔",
        to=os.environ.get("MY_PHONE")
        )
        print(message.status)
        break
