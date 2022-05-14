import os
import smtplib
from email.message import EmailMessage

email_id='mbpawar@mitaoe.ac.in'
email_Pass='22111999@Mayur'

msg=EmailMessage()
msg['Subject']='First mail using python'
msg['From']=email_id
msg['To']=email_Pass
msg.set_content('how about a movie tonight')

for eachfile in os.listdir():
    if eachfile=='pymail.py':
        continue
    with open(eachfile,'rb') as f:
        file_data=f.read()
        file_name=f.name
        msg.add_attachment (file_data,maintype='application',subtype='octet-stream',filename=file_name)


    

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smpt:
    smpt.login(email_id,email_Pass)
    smpt.send_message(msg)