import pandas as pd
from datetime import datetime
import smtplib
import random

email1 = "The Sender email here"
email2 = "The receiving email here"
password = "password for the sender email"

num = random.randint(1, 3)
now = datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("Day32/birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

for birthday in birthdays_dict:
    if (birthday["month"], birthday["day"]) == (month, day):
        with open(f"Day32/letter_templates/letter_{num}.txt") as f:
            letter = f.read().replace("[NAME]", f"{birthday['name']}").replace("[YOUR NAME]", "YOUR NAME HERE")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email1, password=password)
            connection.sendmail(from_addr=email1, to_addrs=email2, msg=f"Subject:Happy Birthday!!\n\n{letter}")