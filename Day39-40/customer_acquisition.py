from dotenv import load_dotenv
import os
from pathlib import Path
import requests

load_dotenv(dotenv_path=Path("./Day39-40/.env"))

print("Welcome to Garrett's Flight Club.\nWe find the best flight deals and email you.") # Replace my name with yours.
first_name = input("What is your first name? \n")
last_name = input("What is your last name? \n")
email = input("What is your email? \n")
confirmation = input("Type your email again. \n")

while email != confirmation:
    print("The emails you entered don't match. Please try again.")
    email = input("What is your email? \n")
    confirmation = input("Type your email again. \n")

if email == confirmation:
    url = os.environ.get("USERS_URL")
    header = {
        'Content_Type': 'application/json', 
        'Authorization': f'Bearer {os.environ.get("BEARER_TOKEN")}' # Optional. Depends on the Authorization you chose.
    }
    body = {
        'user': {
            'firstName': first_name,
            'lastName': last_name,
            'email': email
        }
    }
    response = requests.post(url, json=body, headers=header)
    print("You're in the club!")