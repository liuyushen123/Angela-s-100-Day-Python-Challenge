# Using a .env file to retrieve the phone numbers and tokens.
import os
import smtplib

from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.my_email = os.getenv("GMAIL_USER")
        self.my_password = os.getenv("GMAIL_PASSWORD")

    def send_email(self, message_body, users_list):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)

            for user in users_list["users"]:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=user["whatIsYourEmail?"],
                    msg=f"Subject: New Low Price Flight!\n\n"
                    f"Hi {user['whatIsYourFirstName?']} {user['whatIsYourLastName?']}\n"
                    f"{message_body}".encode("utf-8"),
                )
