import requests
from bs4 import BeautifulSoup
import csv
import json
import Catalog
import telebot

class Parser():
    def __init__(self, userId):
        self.bot = telebot.TeleBot('1756019339:AAFT8q8QqCKQmvT_c7whWtZBJUunWeZzGBA')
        self.HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        self.HOST = 'https://366.ru'
        self.userId = userId

    def get_URL(self,name_subcat):
        cat = Catalog.parse()
        for href in cat:
            if href['text'] == name_subcat:
                return href['href']

    def get_html(self, url, params=None):
        r = requests.get(url, headers=self.HEADERS,params=params)
        return  r

    def get_pages_count(self,html):
        soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
        pagination = soup.find_all('a',class_='b-pagination__item')
        if pagination:
            return int(pagination[-2].get_text())#срез(предпоследний элемент)
        else:
            return 1

    def get_content(self,html):
        soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
        card = soup.find_all('div', class_='listing_product')

        listOfCard = []

        for item in card:
            #a = ' '.join(div[i].get_text().split())
            listOfCard.append({
                'title': self.__Title(item.find('a', class_='listing_product__title')),
                'manufacturer': self.__Manufacturer(item.find('div', class_='listing_product__manufacturer')),
                'elipsis': self.__Elipsis(item.find('div', class_='i-text-ellipsis')),
                'NumberOfPharmacies': self.__NumberOfPharmacies(item.find('div', class_='c-prod-item--product-text')),
                'price': self.__Price(item.find('span', class_='price')),
                'link': self.__Link(item.find('a', class_='listing_product__title')),
                'image': self.__Image(item.find('img', class_='lazyload'))
            })
        return listOfCard

    def __Image(self,item):
        if item:
            item = item.get('data-src')
        else:
            item = None
        return item

    def __Link(self,item):
        if item:
            item = self.HOST + item.get('href')
        else:
            item = None
        return item


    def __Price(self,item):
        if item:
            item = ' '.join(item.get_text().split())
        else:
            item = 'None'
        return item

    def __Title(self,item):
        if item:
            item = ' '.join(item.get_text().split())
        else:
            item = 'None'
        return item

    def __Manufacturer(self,item):
        if item:
            item = ' '.join(item.get_text().split())
        else:
            item = 'None'
        return item

    def __Elipsis(self,item):
        if item:
            item = ' '.join(item.get_text().split())
        else:
            item = 'None'
        return item

    def __NumberOfPharmacies(self,item):
        if item:
            item = ' '.join(item.get_text().split())
        else:
            item = 'None'
        return item

    def save_file(self, items, path):
        with open('Catalog\\'+path, 'w', encoding='utf-8') as file:
            writer =csv.writer(file, delimiter=',')#delimetr=';' - разделитель, для excel открытия
            writer.writerow(['Название', 'Производитель', 'Содержание', 'Количество на складе', 'Цена', 'Ссылка', 'Ссылка на изображение'])
            for item in items:
                writer.writerow([item['title'],item['manufacturer'],item['elipsis'], item['NumberOfPharmacies'],item['price'],item['link'],item['image']])

    def read_json_subcat(self):
        with open("subcat.json", "r", encoding='utf-8') as file:
            data = json.loads(file.read())
            return data


    def parse(self, category, name_file):
        #print(read_json_subcat())
        idMessage = ''
        try:
            URL = self.get_URL(category).strip()
            FILE = name_file
            html = self.get_html(URL)
            if html.status_code == 200:
                medications = []
                pages_count = self.get_pages_count(html.text)
                for page in range(1,pages_count + 1):
                    if idMessage != '':
                        self.bot.delete_message(self.userId, idMessage.id)
                    print(f'Парсинг страницы {page} из {pages_count}')
                    idMessage = self.bot.send_message(self.userId, text=f'Парсинг страницы {page} из {pages_count}')
                    html = self.get_html(URL,params={'page':page})
                    medications.extend(self.get_content(html.text))#extend - расширяет список
                self.save_file(medications, FILE)
            else:
                print('Error')
        except Exception as e:
            print(e)
    #parse('Грипп и простуда','Акушерство и гинекология.csv')
