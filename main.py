# Импорт библиотеки telebot 
import telebot
# Создание переменной с токеном
bot = telebot.TeleBot("5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI")

# Создание кнопки в чате + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,'<b>Привет!</b>',parse_mode = 'html')

# Запуск бота
bot.polling(none_stop = True)
