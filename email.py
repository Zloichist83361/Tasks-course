import smtplib
from checker import check_email

url = 'smtp.yandex.ru'
user = 'pomelov@robotkirov.ru'
password = ''

conn = smtplib.SMTP_SSL(host=url, port=465)
conn.login(user, password)

to_addr = input()
body = input()

if check_email(to_addr, severity=False):
      msg = f'From: {user}\n' \
            f'To: {to_addr}\n' \
            f'Subject: Roman works! \n\n' \
            f'I Nikita!'
      print(msg)
      conn.sendmail(user, to_addr, msg)
else:
      print('Invalid email')
