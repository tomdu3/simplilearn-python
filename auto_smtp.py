import smtplib

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)  # to connect to smtp server
smtp_obj.ehlo()  # to check the connection
smtp_obj.starttls()  # to secure the connection

smtp_obj.login(login, password)  # login to smtp server
