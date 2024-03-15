import telebot
from telebot import types

bot = telebot.TeleBot("7193288200:AAGPuQLljzyS5ZUXVaJN9iY8iiWO1kkbXR4")

@bot.message_handler(commands=['start'])
def start(message):
    #bot.send_message(message.chat.id, 'Привет! Это бот для проверки кпшки на дружбу. Выберите кого хотите проверит.')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Альбинка')
    btn2 = types.KeyboardButton('Саша')
    btn3 = types.KeyboardButton('Максим')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет! Это бот для проверки кпшки на дружбу. Выберите кого хотите проверить.', reply_markup=markup)

@bot.message_handler(content_types= ['text'])
def main(message):
    if message.text == 'Саша':
        bot.send_message(message.chat.id, 'День рождения Саши? (дд.мм.гг)')
        bot.register_next_step_handler(message, next_move)
def next_move(message):
    if message.text == '08.10.07':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, 'Неправильно!')
    bot.send_message(message.chat.id, 'Любимое время года Саши?')
    bot.register_next_step_handler(message, next_move2)
def next_move2(message):
    if message.text == 'весна' or 'Весна':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, 'Неправильно!')
    bot.send_message(message.chat.id, 'Любимая порода собаки у Саши?')
    bot.register_next_step_handler(message, next_move3)
def next_move3(message):
    if message.text == 'корги' or 'Корги':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, 'Неправильно!')
    bot.send_message(message.chat.id, 'Знак зодиака у Саши?')
    bot.register_next_step_handler(message, next_move4)
def next_move4(message):
    if message.text == 'весы' or 'Весы':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, 'Неправильно!')
    bot.send_message(message.chat.id, 'Машина мечты у Саши?')
    bot.register_next_step_handler(message, next_move5)
def next_move5(message):
    if message.text.lower == 'бмв' or 'bmw':
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, 'Неправильно!')
    bot.send_message(message.chat.id, 'Вопросы закончились! Выбери другого!')




# @bot.message_handler(content_types = ['text'])
# def main(message):
#     if message.text == 'Саша':
#         bot.send_message(message.chat.id, 'День рождения Саши? (дд.мм.гг)')
#         bot.register_next_step_handler(message, next_move)
#
# def next_move(message):
#     if message.text == '08.10.07':
#         bot.send_message(message.chat.id, 'Правильно! Любимое время года Саши?')
#         #bot.register_next_step_handler(message, main1)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#     bot.register_next_step_handler(message, next_move1)
# #bot.send_message(message.chat.id, 'Любимое время года Саши?')
#
# #@bot.message_handler(content_types = ['text'])
# # def main1(message):
# #     #while message.text == '08.10.07':
# #         bot.send_message(message.chat.id, )
# #         bot.register_next_step_handler(message, next_move1)
#
# def next_move1(message):
#     if message.text.lower == 'весна':
#         bot.send_message(message.chat.id, 'Правильно!')
#         bot.register_next_step_handler(message, main2)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#         bot.register_next_step_handler(message, main2)
#
# def main2(message):
#     bot.send_message(message.chat.id, 'Любимая порода собаки у Саши?')
#     bot.register_next_step_handler(message, next_move2)
#
# def next_move2(message):
#     if message.text[1].lower == 'корги':
#         bot.send_message(message.chat.id, 'Правильно!')
#         bot.register_next_step_handler(message, main3)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#         bot.register_next_step_handler(message, main3)
#
# def main3(message):
#     bot.send_message(message.chat.id, 'Машина мечты у Саши?')
#     bot.register_next_step_handler(message, next_move3)
#
# def next_move3(message):
#     if message.text.lower == 'бмв' or 'bmw':
#         bot.send_message(message.chat.id, 'Правильно!')
#         bot.register_next_step_handler(message, main4)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#         bot.register_next_step_handler(message, main4)
#
# def main4(message):
#     bot.send_message(message.chat.id, 'Знак зодиака у Саши?')
#     bot.register_next_step_handler(message, next_move4)
#
# def next_move4(message):
#     if message.text.lower == 'весы':
#         bot.send_message(message.chat.id, 'Правильно!')
#         bot.register_next_step_handler(message, main4)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#         bot.register_next_step_handler(message, main4)
#
# def main4(message):
#     bot.send_message(message.chat.id, 'Любимые исполнители у Саши? (название также как на яндекс музыке)')
#     bot.register_next_step_handler(message, next_move5)
#
# def next_move5(message):
#     if message.text.lower == 'lil peep, arctic monkeys, ssshhhiiitt!':
#         bot.send_message(message.chat.id, 'Правильно!')
#         bot.register_next_step_handler(message, main4)
#     else:
#         bot.send_message(message.chat.id, 'Не верно!')
#         bot.register_next_step_handler(message, main4)

bot.polling(none_stop=True)