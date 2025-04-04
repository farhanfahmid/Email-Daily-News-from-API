import smtplib, ssl

def send_email(message):
   host = "smtp.gmail.com"
   port = 465

   username = os.getenv("EMAIL_ADDRESS")
   password = os.getenv("APP_PASS")

   receiver = os.getenv("EMAIL_ADDRESS")
   context = ssl.create_default_context()

   with smtplib.SMTP_SSL(host, port, context=context) as server:
       server.login(username, password)
       server.sendmail(username, receiver, message)
