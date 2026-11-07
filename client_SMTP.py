import smtplib

s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()
s.login("harelnutman@gmail.com", "Hareli11$")
message = "hi "

s.sendmail("harelnutman@gmail.com", "adipele@gmail.com", message)

s.quit()

