import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(email, password)
        server.sendmail(email,receiver_email,message)

