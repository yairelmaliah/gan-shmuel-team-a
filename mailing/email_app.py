import smtplib
from config import *

SENDER_EMAIL = 'develeapproject@gmail.com'
PASSWORD = 'xrrslmjdyjvwddqm'
SERVER_NAME = 'smtp.gmail.com'
SERVER_CODE = 587

def send_email(subject, text, team_leader = None, pusher = None):
    if team_leader == pusher:
        emails = [team_leader]
    else:
        emails = [team_leader,pusher]


    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD)
    print('Login success')
    server.sendmail(SENDER_EMAIL, emails, message)
    print('Email has been sent to ', emails)


