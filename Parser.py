import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://366.ru/c/lekarstva/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
HOST ='https://366.ru'
FILE ='medications.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return  r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
    pagination = soup.find_all('a',class_='b-pagination__item')
    if pagination:
        return int(pagination[-2].get_text())#срез(предпоследний элемент)
    else:
        return 1

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

def save_file(items, path):
    with open(path, 'w', encoding='utf-8') as file:
        writer =csv.writer(file, delimiter=';')#delimetr=';' - разделитель, для excel открытия
        writer.writerow(['Название', 'Производитель', 'Содержание', 'Количество на складе', 'Цена', 'Ссылка', 'Ссылка на изображение'])
        for item in items:
            writer.writerow([item['title'],item['manufacturer'],item['elipsis'], item['NumberOfPharmacies'],item['price'],item['link'],item['image']])

def parse():
    URL = input('Введите URL:')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        medications = []
        pages_count = get_pages_count(html.text)
        for page in range(1,pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}')
            html = get_html(URL,params={'page':page})
            medications.extend(get_content(html.text))#extend - расширяет список
        save_file(medications, FILE)
    else:
        print('Error')
parse()
