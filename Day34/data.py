import requests

# API documentation at opentdb.com/api_config.php
parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(f"https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()['results']