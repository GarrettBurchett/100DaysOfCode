import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.url = os.environ.get("SHEETY_URL")
        self.header = {'Content_Type': 'application/json', 'Authorization': f'Bearer {os.environ.get("BEARER_TOKEN")}'}
        self.destination_data = {}

    def get_rows(self) -> dict:
        response = requests.get(self.url, headers=self.header)
        self.destination_data = response.json()['prices']
        return self.destination_data
    
    def add_row(self, inputs: dict):
        body = {
            'price': inputs
        }
        response = requests.post(self.url, json=body, headers=self.header)
        return response.text
    
    def update_row(self):
        for city in self.destination_data:
            body = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(f"{self.url}/{city['id']}", json=body, headers=self.header)
            print(response.text)

    def get_emails(self):
        customer_endpoint = os.environ.get("USERS_URL")
        response = requests.get(customer_endpoint, headers=self.header)
        self.customer_data = response.json()['users']
        return self.customer_data