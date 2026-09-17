import smtplib


def send_email(name, email, message):
    sender_email = "liuyushen123@gmail.com"
    receiver_email = "liuyushen123@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password="password_placeholder")
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject:New Message from {name}\n\nName: {name}\nEmail: {email}\nMessage: {message}",
        )
