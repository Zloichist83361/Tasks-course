import smtplib
from checker import check_email
from spam_gen import spam

url = 'smtp.yandex.ru'
user = 'chistiakovnr1997@gmail.com'
password = 'mamiunder666'

conn = smtplib.SMTP_SSL(host=url, port=465)
conn.login(user, password)

to_addr = input()
body = input()

print('Enter email:')
to_addr = input()
if check_email(to_addr, severity=False):
    spam
  conn.sendmail(user, to_addr, msg)
else:
      print('Invalid email')

main()