import telebot
from telebot import types

bot = telebot.TeleBot('1756019339:AAFT8q8QqCKQmvT_c7whWtZBJUunWeZzGBA')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
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


#def get_age(message):
    #global age
    #answer = message.text
    # while age == 0: #проверяем что возраст изменился
    #     try:
    #          age = int(message.text) #проверяем, что возраст введен корректно
    #     except Exception:
    #          bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')


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


bot.polling(none_stop=True, interval=0)
