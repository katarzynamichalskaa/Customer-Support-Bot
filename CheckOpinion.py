import requests
from bs4 import BeautifulSoup
import numpy as np

def initRequest(item):

    URL = "https://www.ceneo.pl/"
    requestedURL = URL + ";szukaj-" +str(item)

    return requestedURL

def Find(requestedURL):
    try:
        res = requests.get(requestedURL)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'lxml')
        products = soup.find_all('div', class_='cat-prod-row__content')

        product_info = []

        for product in products:
            name_element = product.find('a', class_='go-to-product js_conv js_clickHash js_seoUrl')
            price_element = product.find('span', class_='price-format nowrap').find('span', class_='value')
            rate_element = product.find('span', class_='product-score')

            if name_element is not None and price_element is not None and rate_element is not None:
                name = name_element.text.strip()
                price_str = price_element.text
                price = int(price_str.replace(" ", "").replace(",", "."))
                rate = rate_element.text.replace('\n5', '').replace('\n', '').replace(' ', '') .replace('/', '')

                if rate != ',0':
                    product_info.append({"name": name, "price": price, "rate": rate})
                    print(f"Product's name: {name}" + f" Price: {price}" + f" Rated: {rate}")


        return product_info

    except Exception as e:
        print(f"Error: {e}")
        return None

def LowestPrice(product_info):
    if product_info is not None:
        sorted_product_info = sorted(product_info, key=lambda x: x['price'])
        print(sorted_product_info)
    else:
        print("product_info is None or empty")

def BestRated(product_info):
    if product_info is not None:
        sorted_product_info = sorted(product_info, key=lambda x: x['rate'], reverse=True)
        print(sorted_product_info)
    else:
        print("product_info is None or empty")
