
# Импорт библиотек для работы
import telebot
import json
import time
from token_bot import key_bot_main
from telebot import *

selfing = False

# Открытие файла stem.json
with open('steam.json','r') as file:
    # Запсиь в переменную файл steam.json
    save_file_main = json.load(file)


# Создание функции

def  save_file():
    text = "myday: happy"
    fp = open('myday.txt', 'a')
    fp.write(text)
    fp.close()








# Указываю боту от кула надо брать токен
bot = telebot.TeleBot(key_bot_main)



# Создание кнопки в чате [start]
@bot.message_handler(commands = ['start'])
# Функция для кнопки start
def start(message):
    # Вывод текста когда будем наживать кнопку
    mess = f'Привет! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    # Указываем в каком расширение будет выводиться текст
    bot.send_message(message.chat.id,mess,parse_mode = 'html')



# Обработка сообщений пользователя
@bot.message_handler()
# Функция по обработке сообщений ползователя
def get_user_text(message):
    global  selfing,save_file
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

    elif message.text == "Вывод файла":
            res = open('myday.txt','r')
            bot.send_message(message.chat.id,res.read())
            res.close()
#
    elif message.text == "Фото":
        bot.send_message(message.chat.id,'Обратный отсчет')

        bot.send_message(message.chat.id,'3')
        time.sleep(1)

        bot.send_message(message.chat.id,'2')
        time.sleep(1)

        bot.send_message(message.chat.id,'1')
        time.sleep(1)

        bot.send_message(message.chat.id,'Фото сделано')
    elif message.text == 'Ты работаешь?':


        bot.send_message(message.chat.id, 'Да я работаю, и постараюсь обработать ваши работы')
    elif message.text == 'Запись в файл':
        bot.send_message(message.chat.id,'Жду!')
        trir = open('myday.txt','a')
        tri = message.text == ''
        trir.write(tri)

    else:
        bot.send_message(message.chat.id,'Не понял)')




# Создание вечного цикла что-бы бот не заканчивал работу
bot.polling(none_stop = True)




