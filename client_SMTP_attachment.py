import smtplib
from email.contentmanager import maintype, subtype

my_email = "harelnutman@gmail.com"
my_password = "hhuc mpoq ycqz acuz"

msg = EmailMessage()

msg['Subject'] = "שליחת SMTP עם קובץ מ- הראל נוטמן"
msg['From'] = my_email
msg['To'] = "adipele@gmail.com"

msg.set_content("הראל נוטמן - \n")

with open("joke.txt", "rb") as f:
    msg.add_attachment(f.read(), maintype = "text", subtype = "plain", filename="joke.txt")

with smtplib.SMTP_SSL('smtp.gmail.com') as s:
    s.login(my_email, my_password)
    s.send_message(msg)
