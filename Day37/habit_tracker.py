import requests
from datetime import date, timedelta
import os
import random
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('./Day37/.env')
load_dotenv(dotenv_path=dotenv_path)

pixela_user_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ.get("USERNAME") 
TOKEN = os.environ.get("TOKEN") # Can randomly generate token by format(random.getrandbits(128), 'x')

user_params = {
    'token': TOKEN, 
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}

# Setup for creating a user on pixela.
# response = requests.post(pixela_user_endpoint, json=user_params)
# print(response.text)

# Setup for creating a graph on Pixela
graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': os.environ.get("GRAPH_ID"),
    'name': 'Step Count Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'sora'
}

HEADER = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=HEADER)
# print(response.text)

# Update my graph to fix the unit of measurement.
update_graph_endpoint = f"{graph_endpoint}/{graph_config['id']}"

update_graph_config = {
    'unit': 'steps'
}
# response = requests.put(update_graph_endpoint, json=update_graph_config, headers=HEADER)
# print(response.text)

yesterday = (date.today() - timedelta(days=1)).strftime('%Y%m%d')

pixel_post_config = {
    'date': yesterday,
    'quantity': "2129"
}

# pixel_response = requests.post(update_graph_endpoint, json=pixel_post_config, headers=HEADER)
# print(pixel_response.text)