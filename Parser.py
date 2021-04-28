import requests
from bs4 import BeautifulSoup
import json

URL = 'https://366.ru/c/lekarstva/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
#'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return  r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
    div = soup.find_all('a', class_='listing_product__title')
    #td = soup.find_all('td')

    percent = []

    for i in range(len(div)):
        a = ' '.join(div[i].get_text().split())
        percent.append({
            'name': a,
        })


    #print(percent)
    #data = json.dumps(percent, ensure_ascii=False)
    #load = json.loads(data)
    #encoding='utf-8'
    # with open("geo-wb-sklad.json", "w", encoding='utf-8') as file:
    #     file.write(data)
    return percent

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Error')
parse()
