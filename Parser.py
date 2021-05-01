import requests
from bs4 import BeautifulSoup
import json

URL = 'https://366.ru/c/lekarstva/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
HOST ='https://366.ru'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return  r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
    card = soup.find_all('div', class_='listing_product')

    listOfCard = []

    for item in card:
        #a = ' '.join(div[i].get_text().split())
        listOfCard.append({
            'title': __Title(item.find('a', class_='listing_product__title')),
            'manufacturer': __Manufacturer(item.find('div', class_='listing_product__manufacturer')),
            'elipsis': __Elipsis(item.find('div', class_='i-text-ellipsis')),
            'NumberOfPharmacies': __NumberOfPharmacies(item.find('div', class_='c-prod-item--product-text')),
            'price': __Price(item.find('span', class_='price')),
            'link': __Link(item.find('a', class_='listing_product__title')),
            'image': __Image(item.find('img', class_='lazyload'))
        })


    #data = json.dumps(percent, ensure_ascii=False)
    #load = json.loads(data)
    #encoding='utf-8'
    # with open("geo-wb-sklad.json", "w", encoding='utf-8') as file:
    #     file.write(data)
    return listOfCard

def __Image(item):
    if item:
        item = item.get('data-src')
    else:
        item = None
    return item

def __Link(item):
    if item:
        item = HOST + item.get('href')
    else:
        item = None
    return item


def __Price(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def __Title(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def __Manufacturer(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def __Elipsis(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def __NumberOfPharmacies(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Error')
parse()
