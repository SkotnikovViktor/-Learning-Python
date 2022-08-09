# Начало работы
# Импорт библиотеки telebot и time
import telebot
import json
import time
import cv2  
# Создание переменной с токеном
bot = telebot.TeleBot('5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI')

with open('file.json','r') as file:
    a = json.load(file)


def cinema():
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    cv2.imwrite('cinemabot.png',frame )
    cap.release()

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
        bot.send_message(message.chat.id,a)
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
        cinema()
        bot.send_message(message.chat.id,'Фото сделано')

    else:
        bot.send_message(message.chat.id,'Опа, а вот это уже не понятно!')

# Создание вечного цикла
# Запуск бота
# АААААААААААААА ошибка в git!
# АААААААААААААА ошибка в git!
bot.polling(none_stop = True)

