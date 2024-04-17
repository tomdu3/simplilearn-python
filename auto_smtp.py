import smtplib

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)  # to connect to smtp server
smtp_obj.ehlo()  # to check the connection
smtp_obj.starttls()  # to secure the connection

smtp_obj.login(login_id, password)  # login to smtp server

from_addr = 'my_email@mail.com'
to_addr = 'destination@mail.com'
msg = '''Subject: Hello world
I greet you humbly.

Sincerely,
Tom
'''

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(login_id, password)

smtp.sendmail(from_addr, to_addr, msg)

smtp.quit()
