def spam(name, date, email, place='Киров'):
    """генерирует спам"""

    s = f"""To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {place}е, которая пройдет {date}."""

    return s

def main():
    print(spam(name='Nikita', date='01.01.2021', email='name1@gmail.com'))

main()
