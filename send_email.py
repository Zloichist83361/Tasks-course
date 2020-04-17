import smtplib
from checker import check_email

def spam(name, date, email, place='Киров'):
    """генерирует спам"""

    s = f"""To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {place}е, которая пройдет {date}."""

    return s

def main():
    print(spam(name='Vladislav', date='01.01.2021', email='chistiakovnr1997@gmail.com'))

main()

url = 'smtp.yandex.ru'
user = #email
password = #password

conn = smtplib.SMTP_SSL(host=url, port=465)
conn.login(user, password)

to_addr = 'pomelov@robotkirov.ru'
#body = input()

if check_email(to_addr, severity=False):
      msg = f'From: {user}\n' \
            f'To: {to_addr}\n' \
            f'Subject: Roman works! \n\n' \
            f'I Nikita!'
      print(msg)
      conn.sendmail(user, to_addr, msg)
else:
      print('Invalid email')
