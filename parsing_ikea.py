from bs4 import BeautifulSoup
import requests as req

links = ['https://www.ikea.com/ru/ru/cat/stolovaya-posuda-18860/',
         'https://www.ikea.com/ru/ru/cat/kuhonnaya-posuda-kt003/',
         'https://www.ikea.com/ru/ru/cat/posuda-dlya-servirovki-16043/',
         'https://www.ikea.com/ru/ru/cat/stakany-bokaly-i-kuvshiny-18868/',
         'https://www.ikea.com/ru/ru/cat/kofe-i-chay-16044/',
         'https://www.ikea.com/ru/ru/cat/stolovye-pribory-18865/']

products_links = []
category = []
products = []


def parser_url(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.findAll('a', ['vn-link vn__nav__link vn-3-grid-gap'
                                'vn-link vn__nav__link vn-4-grid-gap'])
    if result:
        for subcategory in result:
            name_category = subcategory.find('span').getText()
            category.append({'name': name_category})
            parser_url(subcategory.get('href'))
    else:
        product_div = soup.findAll('div', 'range-revamp-product-compact')
        if product_div:
            for product in product_div:
                a = product.find('a')
                products_links.append(a.get('href'))


for link in range(len(links)):
    parser_url(links[link])


for link in range(len(products_links)):
    resp = req.get(products_links[link])
    soup = BeautifulSoup(resp.text, 'html.parser')
    offer_product = soup.find('span', 'range-revamp-product-identifier__number').getText()
    url_product = soup.find('link').get('href')
    name_product = soup.find('div', 'range-revamp-header-section__description').getText()
    price_product = soup.find('span', 'range-revamp-price__integer').getText()
    currency_product = soup.find('span', 'range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript').getText()
    description_product = soup.find('div', 'range-revamp-product-details__container').getText()
    picture_product = soup.find('img').get('srcset')
    param_name_product = soup.find('div', 'range-revamp-header-section__title--big').getText()
    short_description = soup.find('div', 'range-revamp-product-summary').getText()
    materials = soup.find('span', 'range-revamp-product-details__label').getText()
    # size_product = soup.find('div', 'range-revamp-product-dimensions').getText()
    care_instructions = soup.find('div', 'range-revamp-product-details__container').getText()
    information = soup.find('div', 'range-revamp-product-details__container').getText()
    # diameter = soup.find('div', 'range-revamp-product-dimensions__list-container').getText()
    # amount = soup.find('div', 'range-revamp-product-dimensions__list-container').getText()
    products.append({'offer id': offer_product, 'url': url_product, 'name': name_product, 'model': offer_product, 'barcode': offer_product,
                     'price': price_product, 'currencyId': currency_product, 'description': description_product,
                     'picture': picture_product, 'param': [{'name': 'Название IKEA', 'text': param_name_product},
                                                                      {'name': 'Краткое описание', 'text': short_description},
                                                                      {'name': 'Описание.Материалы', 'text': materials},
                                                                      # {'name': 'Описание.Размер товара', 'text': size_product},
                                                                      {'name': 'Описание.Инструкции по уходу', 'text': care_instructions},
                                                                      {'name': 'Описание.Качество и экологическая информация', 'text': materials},
                                                                      {'name': 'Описание.Информация об упаковке', 'text': information}]})
                                                                      # {'name': 'Диаметр', 'text': diameter},
                                                                      # {'name': 'Количество в упаковке', 'text': amount}]})

