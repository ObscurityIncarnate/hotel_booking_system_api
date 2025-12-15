# import the mailjet wrapper
from mailjet_rest import Client
# import os
import environ
# Get your environment Mailjet keys

env = environ.Env()
environ.Env.read_env()


api_key = env("MJ_APIKEY_PUBLIC")
api_secret = env("MJ_APIKEY_PRIVATE")

mailjet = Client(auth=(api_key, api_secret), version="v3")


def send_reservation_change(**kwargs):
    data = {
        "FromEmail": "obscurityincarnate@gmail.com",
        "FromName": "Hoftan Apartments",
        "Subject": f"Your reservation has been {kwargs.get("operation")}!",
        "Text-part": f"Dear {kwargs.get("username")},{kwargs.get("email_body")} You can see all your reservations here: {kwargs.get("user_reservations")}. Best regards, The team.",
        "Html-part": f'<h3>Dear {kwargs.get("username")},<br />{kwargs.get("email_body")} <br /> You can see all your reservations here: <a href="{kwargs.get("user_reservations")}">{kwargs.get("user_reservations")}</a><br />Best regards, <br/> The team.',
        # "Recipients": [{"Email": user.email}],
        "Recipients": [{"Email": kwargs.get("to")}],        
    }
    return mailjet.send.create(data=data)

def send_reservation_create(**kwargs):
    data = {
        "FromEmail": "obscurityincarnate@gmail.com",
        "FromName": "Hoftan Apartments",
        "Subject": f"Your reservation has been {kwargs.get("operation")}!",
        "Text-part": f"Dear {kwargs.get("username")},{kwargs.get("email_body")} You can see all your reservations here: {kwargs.get("user_reservations")}. Best regards, The team.",
        "Html-part": f'<h3>Dear {kwargs.get("username")},<br />{kwargs.get("email_body")} <br /> You can see all your reservations here: <a href="{kwargs.get("user_reservations")}">{kwargs.get("user_reservations")}</a><br />Best regards, <br/> The team.',
        # "Recipients": [{"Email": user.email}],
        "Recipients": [{"Email": kwargs.get("to")}],        
    }
    return mailjet.send.create(data=data)

def send_reservation_delete(**kwargs):
    data = {
        "FromEmail": "obscurityincarnate@gmail.com",
        "FromName": "Hoftan Apartments",
        "Subject": f"Your reservation has been {kwargs.get("operation")}!",
        "Text-part": f"Dear {kwargs.get("username")},{kwargs.get("email_body")} You can see all your reservations here: {kwargs.get("user_reservations")}. Best regards, The team.",
        "Html-part": f'<h3>Dear {kwargs.get("username")},<br />{kwargs.get("email_body")} <br /><br />Best regards, <br/> The team.',
        # "Recipients": [{"Email": user.email}],
        "Recipients": [{"Email": kwargs.get("to")}],        
    }
    return mailjet.send.create(data=data)

def account_signup(**kwargs):
    data = {
        "FromEmail": "obscurityincarnate@gmail.com",
        "FromName": "Hoftan Apartments",
        "Subject": f"Your acount has been created!",
        "Text-part": f"Dear {kwargs.get("username")},{kwargs.get("email_body")} Best regards, The team.",
        "Html-part": f'<h3>Dear {kwargs.get("username")},<br />{kwargs.get("email_body")} <br /><br />Best regards, <br/> The team.',
        # "Recipients": [{"Email": user.email}],
        "Recipients": [{"Email": kwargs.get("to")}],        
    }
    return mailjet.send.create(data=data)