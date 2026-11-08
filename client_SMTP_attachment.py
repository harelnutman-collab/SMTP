#git link - https://github.com/harelnutman-collab/SMTP
import smtplib
from email.message import EmailMessage

my_email = "harelnutman@gmail.com"
my_password = "hhuc mpoq ycqz acuz"

msg = EmailMessage()

msg['Subject'] = "שליחת SMTP עם קובץ מ- הראל נוטמן"
msg['From'] = my_email
msg['To'] = "merrygeva312@gmail.com"

msg.set_content("הראל נוטמן - \n")

with open("joke", "rb") as f:
    msg.add_attachment(f.read(), maintype = "text", subtype = "plain", filename="joke")

with smtplib.SMTP_SSL('smtp.gmail.com') as s:
    s.login(my_email, my_password)
    s.send_message(msg)
