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


def get_catalog(html):
    soup = BeautifulSoup(html,'html.parser')
    catalog = soup.find_all('li', class_='js-facet-item')
    subcat = []
    for cat in catalog:
        href = get_href_subcat(cat.find('a'))
        text = get_text_subcat(cat)
        subcat.append({
            'text':text,
            'href':href
        })
        #print(text + ': '+href)
    return subcat

def get_text_subcat(item):
    if item:
        item = ' '.join(item.get_text().split())
    else:
        item = 'None'
    return item

def get_href_subcat(item):
    if item:
        item = HOST + item.get('href')
    else:
        item = None
    return item


def parse():
    html = get_html(URL.strip())
    if html.status_code == 200:
        cat = get_catalog(html.text)
        return cat
    else:
        print('Error')
        return None
#parse()
