# Импорт библиотеки telebot и time
import telebot
import time 
# Создание переменной с токеном
bot = telebot.TeleBot("5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI")

# Функция которая узнает время
def date_time():
    t= time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    



# Создание кнопки в чате [start] + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,'<b>Привет!</b>',parse_mode = 'html')

# Создание кнопки в чате [help] + вложенная функция
@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id,'<b>Чем я могу помочь вам?</b>',parse_mode = 'html')



# Создание кнопки в чате [help] + вложенная функция
@bot.message_handler(commands = ['time'])
def time(message):
    b = date_time()
    bot.send_message(message.chat.id,b,parse_mode = 'html')




# Запуск бота
bot.polling(none_stop = True)
