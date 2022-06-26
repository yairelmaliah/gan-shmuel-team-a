import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from config import *

def send_mail(send_to, subject, text):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    server = smtplib.SMTP(SERVER_NAME, SERVER_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD)
    try:
      server.sendmail(SENDER_EMAIL, send_to, msg.as_string())
      print(f"Email sent succesfully to: {send_to}", flush=True)
    except:
      print(f"CANT SEND EMAIL TO {send_to}", flush=True)
    server.close()
