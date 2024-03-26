import random
import smtplib
from email.message import EmailMessage

otp = ""
for i in range(6):
    otp += str(random.randint(0,9))

#print(otp)

server =  smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

from_mail = 'dumiiuse@gmail.com'
server.login(from_mail,'rbcn wexa rppp giox')
to_mail = input("enter your email: ")

msg = EmailMessage()
msg['subject'] = "otp verification"
msg['from'] = from_mail
msg['To'] = to_mail
msg.set_content("your otp is: " + otp)

server.send_message(msg)

input_otp = input("Enter OTP: ")
if input_otp == otp:
      print("OTP verified")
else:
      print("invalid otp")

#print("Email sent")