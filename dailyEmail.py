# Imports

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders

# Variables 

username = "auto@belfieldhomeandleisure.co.uk"
password = "I1f7UEmx2B*KEx&cjY0YBQx#A@xQrT"
mail_from = "auto@belfieldhomeandleisure.co.uk"
mail_to = "matt.jones@stability-it.com"
mail_subject = "Daily Documents"
mail_body = "Auto email for the delivery of documents only. Please do not reply to this address."
dir_path = "./"
files = ["test.txt", "test2.txt"]
mail_attachment_names = ["test", "test2"]

# Building email

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))

# Attaching files

for f in files:
    file_path = os.path.join(dir_path, f)
    attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
    attachment.add_header('Content-Disposition','attachment', filename=f)
    mimemsg.attach(attachment)

# Connecting and sending email

connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()