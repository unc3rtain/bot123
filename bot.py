import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot('5921813634:AAHaaFbQwjn4LRVa--wXyhcpxNI0CJH18Yc')

#общее
@bot.message_handler(commands=['start'])
def start(message):
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn21 = types.KeyboardButton (text="Информация о школе")
    btn31 = types.KeyboardButton(text="Адрес школы")
    btn41 = types.KeyboardButton(text="Расписание")
    btn51 = types.KeyboardButton(text="Расписание звонков ")
    kb1.add(btn21, btn31, btn41, btn51)
    bot.send_message(message.chat.id, "Выберите нужную функцию", reply_markup=kb1)
#инфа о школе
@bot.message_handler(content_types='text')
def start(message):
    if message.text == "Информация о школе":
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Показать оффициальный сайт школы", url='https://angarsk27.ru/')
        btn2 = types.InlineKeyboardButton(text="Показать оффициальную группу школы", url='https://vk.com/school_27_angarsk/')
        kb.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите нужную кнопку", reply_markup=kb)
    elif message.text == "Адрес школы":
        qw = types.InlineKeyboardMarkup(row_width=1)
        qw1 = types.InlineKeyboardButton(text="Показать адрес школы", url='https://goo.su/UNfq')
        qw.add(qw1)
        bot.send_message(message.chat.id, "Нажмитке на кнопку для перехода ", reply_markup=qw)
    elif message.text == "Расписание":
        qz = types.InlineKeyboardMarkup(row_width=1)
        qz1 = types.InlineKeyboardButton(text="Показать актуальное расписание школы", url='https://vk.com/the_best_school_in_the_world_27')
        qz.add(qz1)
        bot.send_message(message.chat.id, "Нажмитке на кнопку для перехода", reply_markup=qz)
    elif message.text == "Расписание звонков":
        bot.send_photo(message.chat.id, "https://vk.com/the_best_school_in_the_world_27?z=photo-61541001_457240900%2Falbum-61541001_182930438%2Frev")

bot.polling(none_stop=True, interval=0)
