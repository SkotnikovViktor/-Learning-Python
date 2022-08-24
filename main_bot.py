# Начало работы
# Импорт библиотеки telebot и time
import telebot
import json
import time
from main_bot_token import key_bot_main
# Создание переменной с токеном

with open('main_file_json.json','r') as file:
    save_file_main = json.load(file)


bot = telebot.TeleBot(key_bot_main)

# Создание кнопки в чате [start] + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode = 'html')


# Обработка сообщений пользователя + вложеная функция
@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет!':
        bot.send_message(message.chat.id,'Привет мой друг!')
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id,'Нормально')
    elif message.text == 'Steam':
        bot.send_message(message.chat.id,save_file_main )
    elif message.text == 'Hello':
        bot.send_message(message.chat.id,'Нi!')
    elif message.text == 'Name?':
        bot.send_message(message.chat.id, 'BotOnPython!')
    elif message.text == 'Калькулятор!':
        bot.send_message(message.chat.id,'Выберите сложение, вычитание, умножение или деление')
    elif message.text == "/help":
        bot.send_message(message.chat.id,'Я буду рад вам помочь!)')
    elif message.text == "Фото":
        bot.send_message(message.chat.id,'Обратный отсчет')
        bot.send_message(message.chat.id,'3')
        time.sleep(1)
        bot.send_message(message.chat.id,'2')
        time.sleep(1)
        bot.send_message(message.chat.id,'1')
        time.sleep(1)
        bot.send_message(message.chat.id,'Фото сделано')

    else:
        bot.send_message(message.chat.id,'Опа, а вот это уже не понятно!')

# Создание вечного цикла
# Запуск бота
bot.polling(none_stop = True)

