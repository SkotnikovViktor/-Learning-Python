# Импорт библиотеки telebot и time
import telebot
import json
# Создание переменной с токеном
bot = telebot.TeleBot('5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI')

with open('file.json','r') as file:
    file_json = json.load(file)
    

# Создание кнопки в чате [start] + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode = 'html')



# Калькулятор (Добавлен только алгоритм работы(калькулятор не работает!))
@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет!':
        bot.send_message(message.chat.id,'Привет мой друг!')
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id,'Нормально')
    elif message.text == 'Steam':
        bot.send_message(message.chat.id,file_json)
    elif message.text == 'Hello':
        bot.send_message(message.chat.id,'Нi!')
    elif message.text == 'Name?':
        bot.send_message(message.chat.id, 'BotOnPython!')
    elif message.text == 'Калькулятор!':
        bot.send_message(message.chat.id,'Выберите сложение, вычитание, умножение или деление')
    else:
        bot.send_message(message.chat.id,'Опа, а вот это уже не понятно!')

            
# Запуск бота
bot.polling(none_stop = True)

