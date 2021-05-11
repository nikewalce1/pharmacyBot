import telebot
from telebot import types
import Parser

bot = telebot.TeleBot('1756019339:AAFT8q8QqCKQmvT_c7whWtZBJUunWeZzGBA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Каталог')
    markup.add(button1)
    bot.send_message(message.chat.id, "Выберите нужный!", reply_markup=markup)

@bot.message_handler(commands=['view'])
def view(message):
    get_catalog(message.from_user.id)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    CATALOG = ['Акушерство и гинекология', 'Аллергия', 'Инфекционные и вирусные заболевания', 'Дыхательная система',
               'Грипп и простуда', 'Грипп и простуда', 'Противовоспалительные и обезболивающие средства',
               'Желудочно-кишечный тракт и печень', 'Сердечно-сосудистая система',
               'Неврологические и психические заболевания', 'Мочеполовая система и почки',
               'Дерматологические заболевания', 'Онкологические заболевания', 'Эндокринные заболевания',
               'Глазные и ушные капли', 'Лекарственные травы', 'Иммунитет', 'Гомеопатия', 'Обмен веществ',
               'Препараты для анестезии, реанимации, трансфузий', 'Диабет', 'Спазмолитики']
    print(message.text)
    if message.text == "Каталог":
        get_catalog(message.from_user.id)
    if message.text in CATALOG:
        category = message.text
        name_file = message.text.replace(' ','') + '.csv'
        print(category + ' ' + name_file)
        bot.send_message(message.from_user.id, text='Подождите... Идет сбор информации...')
        Parser.parse(category,name_file,message.from_user.id)
        bot.send_message(message.from_user.id, text='Сбор закончен!')

    if message.text == '/sstart':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_head = types.InlineKeyboardButton(text='Голова', callback_data='head')  # кнопка «Да»
        keyboard.add(key_head)  # добавляем кнопку в клавиатуру
        key_stomach = types.InlineKeyboardButton(text='Живот', callback_data='stomach')
        keyboard.add(key_stomach)

        question = 'Выберите место, которое болит!'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        #--------Локация-----------------
        # keyboardReply = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        # button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        # keyboardReply.add(button_geo)
        # bot.send_message(message.chat.id, reply_markup=keyboardReply)

def get_catalog(id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Акушерство и гинекология')
    button2 = types.KeyboardButton('Аллергия')
    button3 = types.KeyboardButton('Инфекционные и вирусные заболевания')
    button4 = types.KeyboardButton('Дыхательная система')
    button5 = types.KeyboardButton('Грипп и простуда')
    button6 = types.KeyboardButton('Противовоспалительные и обезболивающие средства')
    button7 = types.KeyboardButton('Желудочно-кишечный тракт и печень')
    button8 = types.KeyboardButton('Сердечно-сосудистая система')
    button9 = types.KeyboardButton('Неврологические и психические заболевания')
    button10 = types.KeyboardButton('Мочеполовая система и почки')
    button11 = types.KeyboardButton('Дерматологические заболевания')
    button12 = types.KeyboardButton('Онкологические заболевания')
    button13 = types.KeyboardButton('Эндокринные заболевания')
    button14 = types.KeyboardButton('Глазные и ушные капли')
    button15 = types.KeyboardButton('Лекарственные травы')
    button16 = types.KeyboardButton('Иммунитет')
    button17 = types.KeyboardButton('Гомеопатия')
    button18 = types.KeyboardButton('Обмен веществ')
    button19 = types.KeyboardButton('Препараты для анестезии, реанимации, трансфузий')
    button20 = types.KeyboardButton('Диабет')
    button21 = types.KeyboardButton('Спазмолитики')
    markup.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12, button13, button14,button15,button16,button17,button18,button19,button20,button21)
    bot.send_message(id, "Каталог", reply_markup=markup)

def get_pills(call,name_of_pain):
    stomach_pills = {
        "1. Но-шпа":"Pictures\\No_shpa.jpg",
        "2. Панкреатин":"Pictures\\pankreatin.jpg",
        "3. Метоклопрамид":"Pictures\\metoclopramid.jpg",
        "4. Маалокс":"Pictures\\maaloks.png",
        "5. Дюспаталин":"Pictures\\duspatalin.jpg",
        "6. Мотилиум":"Pictures\\motilium.jpg",

    }
    head_pills = {
        "1. Панадол": "Pictures\\panadol.jpg",
        "2. Спазмалгон": "Pictures\\spazmalgon.jpg",
        "3. Ибупрофен": "Pictures\\ibuprofen.jpg",
        "4. Аспирин С": "Pictures\\aspirin.jpg",
        "5. Парацетамол": "Pictures\\paracetamol.jpg",
        "6. Пенталгин": "Pictures\\pentalgin.jpg",

    }
    if name_of_pain == "stomach":
        for key in stomach_pills:
            print(key, '->', stomach_pills[key])
            bot.send_message(call.message.chat.id, key)
            #bot.send_photo(call.message.chat.id, stomach_pills[key])
            bot.send_photo(call.message.chat.id, photo = open('{}'.format(stomach_pills[key]), 'rb'))
    elif name_of_pain == "head":
        for key in head_pills:
            print(key, '->', head_pills[key])
            bot.send_message(call.message.chat.id, key)
            #bot.send_photo(call.message.chat.id, head_pills[key])
            bot.send_photo(call.message.chat.id, photo=open('{}'.format(head_pills[key]), 'rb'))

    # bot.send_photo(chat_id, photo=open('path', 'rb'))#путь к изображению


# @bot.message_handler(content_types=["location"])
# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "head":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Головные боли')
        get_pills(call, "head")
    elif call.data == "stomach":
        bot.send_message(call.message.chat.id, 'Боли в животе')
        #---------------------------
        get_pills(call,"stomach")
    elif call.data =="category":
        bot.send_message(call.message.chat.id,"Категории:")


bot.polling(none_stop=True, interval=0)
