import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


print('Starting to make a photo.')
subprocess.call(['fswebcam', 'file.jpg'])
print('Image saved')
print('Ready to send the email')
email_sender = 'bobbyphoto@aol.com'
email_receiver = 'johnson.1484@wright.edu'
subject = 'weight'
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject']= subject
body = 'this is the weight screenshot of the raspberry pi'
msg.attach(MIMEText(body, 'plain'))

#FILE PART
filename = 'file.jpg'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet_stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= '+filename)
msg.attach(part)
#########

text = msg.as_string()
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(email_sender, '26Iforgot')
connection.sendmail(email_sender, email_receiver, text )
connection.quit()
print('email sent')
