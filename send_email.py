import smtplib , ssl
import os

def email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "lchetanreddy2001@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "lchetanreddy2001@gmail.com"


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail( username, receiver, message )