import requests
import os
from flight_data import FlightData

TEQUILA_URL = "https://api.tequila.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key = os.environ.get("FLIGHT_API_KEY")
    
    def get_destination_code(self, city_name):
        header = {
            'accept': 'application/json',
            'apikey': self.api_key
        }
        query = {
            'term': city_name,
            'location_types': "city"
        }
        response = requests.get(url=f"{TEQUILA_URL}/locations/query", headers=header, params=query)
        location_data = response.json()['locations']
        return location_data[0]['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            'accept': 'application/json',
            'apikey': self.api_key
        }
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time,
            'date_to': to_time,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopovers': 0,
            "curr": "USD"
        }
        response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=header, params=query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            query['max_stopovers'] = 1
            response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=header, params=query)
            
            try:
                data = response.json()['data'][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
            else:
                flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data