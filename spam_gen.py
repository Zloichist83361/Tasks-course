def spam(name, date, email, place='Киров'):
    """ генерирует спам """

    s = f'''
    To: {email}
    Здравствуйте, {name}!
    Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {date}.
    '''

    return s


def main():
    print(spam(name='Vladislav', place='Кирово-Чепецк', date='01.01.2021', email='100xp@rambler.ru'))
    print(spam(name='Vladislav', date='01.01.2021', email='100xp@rambler.ru'))
    print(spam('Vladislav', '01.01.2020', '111@111.ru'))


main()