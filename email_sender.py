import smtplib, ssl
import streamlit as st

# # Your Formspree endpoint
# FORMSPREE_URL = "https://formspree.io/f/mnnpnozd"


def send_email(message):
   host = "smtp.gmail.com"
   port = 465

   username = "fahmidfarhan2758@gmail.com"
   password = "roes lurs vbfj thzo"

   receiver = "fahmidfarhan2758@gmail.com"
   context = ssl.create_default_context()

   with smtplib.SMTP_SSL(host, port, context=context) as server:
       server.login(username, password)
       server.sendmail(username, receiver, message)