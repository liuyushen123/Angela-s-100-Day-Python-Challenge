import datetime as dt
import random
import smtplib

my_email = "liuyushen123@gmail.com"
my_password = "dscsgxbhdqmghqff"


def send_message(subjct, quote, author, target_email):
    user_message = f"Subject:{subjct}\n\n{quote.strip()}\n\n{' ' * 70}{author.strip()}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=user_message,
        )


sam_date_of_birth = dt.datetime(
    year=2006,
    month=9,
    day=11,
)

with open("quotes.txt") as file:
    message_to_send = file.readlines()
    quote, author = random.choice(message_to_send).split("-")
    send_message(
        "Keep it up!",
        quote,
        author,
        "32923146@nebraska.edu",
    )
