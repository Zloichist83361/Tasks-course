import requests
from bs4 import BeautifulSoup
import time

class Currency:
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk027aoDBaiT01uiVX84hqRjHY-3LVA%3A1586174714975&ei=-hqLXuiRO8i21fAP8vy4SA&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83&gs_lcp=CgZwc3ktYWIQAxgAMgkIABBDEEYQggIyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6BAgjECc6BAgAEENKMAgXEiwwZzIwMmcyMTJnMjU0ZzIwMGcxODRnMTgzZzIwMmcyMzZnMjE0ZzE5NmcyMkobCBgSFzBnMWcxZzFnMWcxZzFnMWcxZzFnMmc1UOKCAVj7jwFg6JgBaABwBXgAgAHxAYgB8xCSAQUwLjYuNZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(',', '.' ))
    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(',', '.' ))
        if currency >= self.current_converted_price + self.difference:
            print('Курс сильно вырос, может пора что-то делать?')
        elif currency <= self.current_converted_price - self.difference:
            print('Курс сильно упал, может пора что-то делать?')
        print('Сейчас курс: 1 доллар = ' + str(currency))
        time.sleep(3)
        self.check_currency( )

currency = Currency()
currency.check_currency()

