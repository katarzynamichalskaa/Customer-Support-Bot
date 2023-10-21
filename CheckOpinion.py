import requests
from bs4 import BeautifulSoup

def initRequest(item):

    URL = "https://www.ceneo.pl/"
    requestedURL = URL + ";szukaj-"+str(item)

    return requestedURL

def Find(requestedURL):

    try:
        res = requests.get(requestedURL)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'lxml')
        products = soup.find_all('div',
                                 class_='cat-prod-row__content')

        product_info = []

        for product in products:
            name = product.find('a', class_='go-to-product js_conv js_clickHash js_seoUrl').text
            price_str = str(product.find('span', class_='price-format nowrap').find('span', class_='value').text)
            price = int(price_str.replace(" ", "").replace(",", "."))

            product_info.append({name, price})
            print(f"Nazwa produktu: {name}" + f"cena: {price}")

        return product_info


    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None

def CheckLowestPrice(product_info):
    print(product_info)
    if product_info is not None:
        sorted_product_info = sorted(product_info, key=lambda x: x['price'])
        print(sorted_product_info)
    else:
        print("product_info is None or empty")
