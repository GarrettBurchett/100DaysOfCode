import smtplib
from datetime import datetime
import random

email1 = "The Sender email here"
email2 = "The receiving email here"
password = "password for the sender email"
now = datetime.now()

with open("Day32/quotes.txt") as f:
    quotes = f.readlines()

chosen_quote = random.choice(quotes)
print(now.weekday())

if now.weekday() == 5:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email1, password=password)
        connection.sendmail(from_addr=email1, to_addrs=email2, msg=f"Subject:Motivational Quote\n\n.{chosen_quote}")