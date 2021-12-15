import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = "auto@belfieldhomeandleisure.co.uk"
password = "I1f7UEmx2B*KEx&cjY0YBQx#A@xQrT"
mail_from = "auto@belfieldhomeandleisure.co.uk"
mail_to = "matt.jones@stability-it.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"
mail_attachment= "c:\Users\matt.jones\Desktop\test.txt"
mail_attachment_name= "test.txt"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))

with open(mail_attachment, "rb") as attachment:
    mimefile = MIMEBase('application', 'octet-stream')
    mimefile.set_payload((attachment).read())
    encoders.encode_base64(mimefile)
    mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
    mimemsg.attach(mimefile)
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()