# Imports

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import keyring
# The password will need to have been added into the credentials manager of the system running the script before the keyring.get_password will work. This is done by, in a python terminal, typing "import keyring" followed by "keyring.set_password("nameOfStoredPassword", "usernameOfStoredPassword", "password")". You can check that this has worked by entering "keyring.get_password("nameOfStoredPassword", "usernameOfStoredPassword")" which should return the password provided. 

# Variables 

username = "email@domain.com"
password = "app password"
mail_from = "email@domain.com"
mail_to = "addressee@domain.com"
mail_subject = "Email Subject"
# Triple quotes for multiline strings if required
mail_body = """Auto email for the delivery of documents only. Please do not reply to this address."""
# If using Windows remember the escaping \
dir_path = "./"
files = ["test.txt", "test2.txt"]
file_names = ["test.txt", "test2.txt"]
i = 0

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
    attachment.add_header('Content-Disposition','attachment', filename=f"{file_names[i]}")
    mimemsg.attach(attachment)
    i = i + 1

# Connecting and sending email

connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,keyring.get_password("autoemail", "email@domain.com"))
connection.send_message(mimemsg)
connection.quit()