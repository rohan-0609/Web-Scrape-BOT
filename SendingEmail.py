import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_add = 'aggarwal.rohan2402@gmail.com'
To_add = 'rohanraj.aggarwal@gmail.com'
subject = 'Emailing with Python script'

msg = MIMEMultipart()
msg['From'] = from_add
msg['To'] = To_add
msg['Subject'] = subject

body = "<b>Hello, I tried sending this email with python script !!</b>" # html tag

msg.attach(MIMEText(body, 'html')) # can be turned in html over plain

my_file = open("stocks.csv", 'rb')

part = MIMEBase('application', 'octet - stream')
part.set_payload((my_file).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename=' + 'stocks.csv')
msg.attach(part)

message = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_add, 'qoxsujnvdzcbahxq')

server.sendmail(from_add, To_add, message)

print("Email sent !!")
server.quit()
