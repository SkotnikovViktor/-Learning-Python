# Импорт библиотеки telebot и time
import telebot
import time 
# Создание переменной с токеном
bot = telebot.TeleBot("5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI")

# Функция которая узнает время
def date_time():
    t= time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    return current_time
    

# Создание кнопки в чате [start] + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode = 'html')


# Обработка чата и вывод времени 
@bot.message_handler()
def get_user_text(message):
    if message.text == 'time':
        b = str(date_time())
        bot.send_message(message.chat.id,b,parse_mode = 'html')



# Запуск бота
bot.polling(none_stop = True)
