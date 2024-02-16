import telebot
from translate import Translator

bot = telebot.TeleBot('6736234157:AAHsfybZwIWSBOrbTM7BGvVGa1JLiV4qkj0')

rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
eng = 'abcdefghijklmnopqrstuvwxyz'

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Это бот для перевода текста с английского на русский и наоборот.')
    bot.send_message(message.chat.id, 'Введите текст для перевода')

@bot.message_handler(content_types = ['text'])
def get_rext(message):
    mt = message.text
    if mt[0].lower() in rus:
            translator =  Translator(from_lang="russian", to_lang="english")
            tr = translator.translate(mt)
            bot.reply_to(message, tr)
    else:
            translator = Translator(from_lang="english", to_lang="russian")
            tr = translator.translate(mt)
            bot.reply_to(message, tr)
        
bot.polling(non_stop=True)