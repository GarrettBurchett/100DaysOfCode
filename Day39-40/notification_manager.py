import smtplib
import os
# from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = os.environ.get("EMAIL")
        # self.account = os.environ.get("TWILIO_ACCOUNT")
        # self.auth_token = os.environ.get("AUTH_TOKEN")
        # self.from_number = os.environ.get("TWILIO_PHONE")
        # self.to_number = os.environ.get("MY_PHONE")
        
    def send_email(self, notification):    
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=os.environ.get("EMAIL_APP_PASSWORD"))
                connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=f"Subject:Low Price Alert!\n\n{notification}")

    # def send_text(self, notification):
    #     client = Client(self.account, self.auth_token)

    #     message = client.messages.create(
    #         from_=self.from_number,
    #         body=notification,
    #         to=self.to_number
    #         )
    #     print(message.sid)
                
    def send_emails(self, message, emails):
         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=os.environ.get("EMAIL_APP_PASSWORD"))
                for email in emails:
                    connection.sendmail(from_addr=self.email, to_addrs=email, msg=f"Subject:Low Price Alert!\n\n{message}")