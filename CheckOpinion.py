import requests
from bs4 import BeautifulSoup
import numpy as np
from tabulate import tabulate

class WebRequester:
    def initRequest(self, item):
        URL = "https://www.ceneo.pl/"
        requestedURL = URL + ";szukaj-" +str(item)

        return requestedURL
    def Find(self, requestedURL):
        try:
            res = requests.get(requestedURL)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, 'lxml')
            products = soup.find_all('div', class_='cat-prod-row__content')
            list_of_products = self.Lists(products)
            return list_of_products

        except Exception as e:
            print(f"Error: {e}")
            return None

    def Lists(self, products):
        product_info = []

        for product in products:
            name_element = product.find('a', class_='go-to-product js_conv js_clickHash js_seoUrl')
            price_element = product.find('span', class_='price-format nowrap').find('span', class_='value')
            rate_element = product.find('span', class_='product-score')

            if name_element is not None and price_element is not None and rate_element is not None:
                name = name_element.text.strip()
                price_str = price_element.text
                price = int(price_str.replace(" ", "").replace(",", "."))
                rate = rate_element.text.replace('\n5', '').replace('\n', '').replace(' ', '').replace('/', '')

                if rate != ',0':
                    product_info.append({"name": name, "price": price, "rate": rate})
        return product_info

    def LowestPrice(self, product_info):
        if product_info is not None:
            sorted_product_info = sorted(product_info, key=lambda x: x['price'])
            table = tabulate(sorted_product_info, headers="keys", tablefmt="pretty")
            print(table)
        else:
            print("product_info is None or empty")

    def BestRated(self, product_info):
        if product_info is not None:
            sorted_product_info = sorted(product_info, key=lambda x: x['rate'], reverse=True)
            table = tabulate(sorted_product_info, headers="keys", tablefmt="pretty")
            print(table)
        else:
            print("product_info is None or empty")
