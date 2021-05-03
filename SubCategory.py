import requests
from bs4 import BeautifulSoup
import Catalog
import json

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
HOST ='https://366.ru'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return  r

def get_URL(name_subcat):
    cat = Catalog.parse()
    if cat:
        for href in cat:
            if href['text'] == name_subcat:
                return href['href']
    else:
        return None

def get_catalog(html):
    soup = BeautifulSoup(html,'html.parser')
    catalog = soup.find_all('li', class_='subcategories__item')
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

def save_to_file():
    list = parse()
    data = json.dumps(list, ensure_ascii=False)
    with open("subcat.json", "w", encoding='utf-8') as file:
        file.write(data)


def parse():
    cat = []
    for key in Catalog.parse():
        URL = get_URL(key['text']).strip()
        html = get_html(URL.strip())
        if html.status_code == 200:
            cat.append({
                'Category': key['text'],
                'SubCategory': get_catalog(html.text)
            })
        else:
            cat = cat.append(None)
    return cat
parse()
#save_to_file()
