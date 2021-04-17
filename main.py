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
        "1. Но-шпа":"https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3233-6633-4965-a437-396236393134__1.jpg",
        "2. Панкреатин":"https://compendium.com.ua/img/inf/pankreatin_60tab.jpg",
        "3. Метоклопрамид":"https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild6532-3664-4834-b161-393437363263__2.jpg",
        "4. Маалокс":"https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3834-3135-4633-b139-656439373266__3.jpg",
        "5. Дюспаталин":"https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3932-3162-4234-b037-363862313038__4.jpg",
        "6. Мотилиум":"https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild6637-6131-4266-b565-393739383161__5.jpg",

    }
    head_pills = {
        "1. Панадол": "https://aptekanc.com/content/images/thumbs/0017944_panadol-tabl-500-mg-12-glaksosmitkljn_1.jpg",
        "2. Спазмалгон": "https://media.add.ua/media/catalog/product/cache/1/image/720x/9df78eab33525d08d6e5fb8d27136e95/s/p/spazmalgon_n50_01/add.ua-balkanpharma-dupnitza-(bolgarija)-spazmalgon-500-mg-tabletki-%E2%84%9650-34.jpg",
        "3. Ибупрофен": "https://maksavit.ru/upload/iblock/371/371403a02ed8c7c3c36cf9e217fd8508.jpg",
        "4. Аспирин С": "https://maksavit.ru/upload/iblock/d51/d516346dc1f2163053808d790e437ce4.jpg",
        "5. Парацетамол": "https://maksavit.ru/upload/iblock/653/6532cd17b822a6dc73f76b388f5559a0.jpg",
        "6. Пенталгин": "https://maksavit.ru/upload/iblock/329/329cc5c9d26c5b4fef74f5595f75c4d4.jpg",

    }
    if name_of_pain == "stomach":
        for key in stomach_pills:
            print(key, '->', stomach_pills[key])
            bot.send_message(call.message.chat.id, key)
            bot.send_photo(call.message.chat.id, stomach_pills[key])
    elif name_of_pain == "head":
        for key in head_pills:
            print(key, '->', head_pills[key])
            bot.send_message(call.message.chat.id, key)
            bot.send_photo(call.message.chat.id, head_pills[key])


    # bot.send_photo(chat_id, photo=open('path', 'rb'))#путь к изображению


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
