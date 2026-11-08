#git link - https://github.com/harelnutman-collab/SMTP
import smtplib

from email.message import EmailMessage

my_email = "harelnutman@gmail.com"
my_password = "hhuc mpoq ycqz acuz"

msg = EmailMessage()

msg['Subject'] = "שליחת SMTP מ-הראל נוטמן"
msg['From'] = my_email
msg['To'] = "merrygeva312@gmail.com"

msg.set_content("הראל נוטמן - תימני אחד עומד למות שוכב במיטה שואל את אשתו מזל את כאן? היא עונה בדמעות כן אני פה, שואל את הילדים שלו: בנים שלי אתם פה? הם עונים אנחנו פה לידך אבא, שואל את כל הנכדים שלו כולם פה? עונים לו: כן כולנו פה, הוא אומר: אז למה האור בשירותים דולק?")

with smtplib.SMTP_SSL('smtp.gmail.com') as s:
    s.login(my_email, my_password)
    s.send_message(msg)
