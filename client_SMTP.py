import smtplib

from email.message import EmailMessage

my_email = "harelnutman@gmail.com"
my_password = "hhuc mpoq ycqz acuz"

msg = EmailMessage()

msg['Subject'] = "שליחת SMTP מ-הראל נוטמן"
msg['From'] = my_email
msg['To'] = "adipele@gmail.com"

msg.set_content("הראל נוטמן - ")

with smtplib.SMTP_SSL('smtp.gmail.com') as s:
    s.login(my_email, my_password)
    s.send_message(msg)
