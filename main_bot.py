# !Бот, а также приложение находиться в разработке, и может работать не правильно или вообще не работать!
# !Данный файл не может работать один(в разрешение .py), если будете запускать его в .py файле то обязательно нужно взять файл function.py!

# Последнее редактирование было 16.07.2023
# Импорт нужных библиотек для работы
import getpass
import os
from pathlib import Path
from ctypes import *
import ctypes
import subprocess
import sys
import webbrowser
import time
from telebot import *
from os import remove
from function import *
from datetime import datetime
from datetime import *
from PIL import Image
import easygui as e
import getpass
import os


# Пока не точно(нвр нужно будет убрать! И надо закинуть в файл apps.py(apps.exe))
# Запуск приложения от имени админа
#if not ctypes.windll.shell32.IsUserAnAdmin():
#    print("not an admin, restarting...")
#    subprocess.run(["launcher.exe", sys.executable, *sys.argv])
#else:
#    print("I'm an admin now.")

# Создание Папок, Файлов для отслежки информации
#Path("C:/Program Files/PersonControle").mkdir(parents=True, exist_ok=True)
#os.path.isfile(r'C:/Program Files/PersonControle/false.txt')
#os.path.isfile(r'C:/Program Files/PersonControle/token.txt')
#file_false = open('C:/Program Files/PersonControle/false.txt','w')
#file_false.write('0')
#file_token = open('C:/Program Files/PersonControle/token.txt','w')
#file_false.close()
#file_token.close()





# Создание файла .bat для автозапуска приложения (при запуске Пк)
USER_NAME = getpass.getuser()
def add_to_startup(file_path="C:/Program Files/PersonControle/main_bot.exe"):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)
add_to_startup()







# Проверка файла на 1 или 0, если 1 то пропуск участка кода, а если 0 то запускаем приложение--
# Которое внесёт в файл токен для работы бота
file = open('false.txt','r')
falsing = file.read()
if str(falsing)=='0':
    startfile("apps.exe")
    bot = telebot.TeleBot('5780822869:AAEfbm0nL0YkZEof_lkv70qdBAbuKXkAQwo')
else:
    file_token = open('token.txt','r')
    file_token_bot = file_token.read()
    bot = telebot.TeleBot(file_token_bot)
    file_token.close()
file.close()



# Основной код БОТА, а также кнопка "start"
@bot.message_handler(commands = ['start'])
# Создание кнопок для быстрого функционала в боте
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Выключить ПК!')
    item2 = types.KeyboardButton('Открыть PyCharm!')
    item3 = types.KeyboardButton('Открыть SublimeText!')
    item4 = types.KeyboardButton('Открыть Yandex!')
    item6 = types.KeyboardButton('Точное время!')
    item7 = types.KeyboardButton('Перезагрузить ПК!')
    item8 = types.KeyboardButton('Ввести ПК в спящий режим!')
    item9 = types.KeyboardButton('Курс Доллара$.')
    item10 = types.KeyboardButton('Курс Евро€.')
    item11 = types.KeyboardButton('Открой мне Arizona')
    item12 = types.KeyboardButton('Курс Рубля₽.')
    item13 = types.KeyboardButton('Скриншот экрана.')
    item5 = types.KeyboardButton('Ничего, не нужно.')
    markup.add(item1,item2,item3,item4,item11,item6,item7,item8,item9,item10,item12,item5,item13)
    bot.send_message(message.chat.id,'Здравствуйте, {0.first_name}!'.format(message.from_user),reply_markup=markup)



# Обработка сообщений пользователя
@bot.message_handler(content_types=['text'])
# Функция по обработке сообщений ползователя
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Выключить ПК!':
            # Вызываем функцию для выключения ПК!
            shutdown()
            # Делаем тайм-аут, для того, чтобы ожидать пока завершиться сеанс в течении 1 минуты
            sleep(45)
            # Отправляем сообщение пользователю о том,что его ПК был выключен!
            bot.send_message(message.chat.id,'Ваш, ПК был успешно выключен! Можете спать спокойно, за вами следит мальенький БетМен<3!')

        elif message.text == 'Открыть PyCharm!':
            # Вызываем функцию для открытия приложения (PyCharm)
            open_PyCharm()
            # Отправляем сообщение пользователю о выолненой работе открытие приложения
            bot.send_message(message.chat.id,'Сделано!')
        elif message.text == 'Открыть SublimeText!':
            # Вызываем функцию для открытия приложения (SublimeText)
            open_SublimeText()
            # Отправляем сообщение пользователю о выполненой работе, по открытию приложения
            bot.send_message(message.chat.id, 'Сделано! Приятного программирования!')

        elif message.text == 'Ничего, не нужно.':
            bot.send_message(message.chat.id,'Хорошо, буду ждать ваших комманд! Если, что я всегда готов!')
    
        elif message.text == "Открыть Yandex!":
            open_Yandex()
            bot.send_message(message.chat.id, 'Сделано! Приятного сёрфинга в интернете!')

        elif message.text == 'Точное время!':
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            bot.send_message(message.chat.id,current_time)
            bot.send_message(message.chat.id, 'Ловите точное время, по МСК! Никогда не опаздывайте, тем более к близким они вас любят<3!')

        elif message.text == 'Ввести ПК в спящий режим!':
            bot.send_message(message.chat.id, 'ПК был введён с спящий режим! Можете не беспокоиться я его буду охранять!')
            sleep(5)
            sleep_system()

        elif message.text == 'Скриншот экрана.':
            screen()
            img = Image.open('screenshot.png')
            bot.send_message(message.chat.id, 'Опа! Ловите скрин, но только давайте договримся, вы меня не знаете, а я вас. Удачи<3')
            bot.send_message(message.chat.id,'Извините за плохое качество! Это проблема теллеграма!)')
            bot.send_photo(message.chat.id,img)
            sleep(2)
            remove('screenshot.png')
        elif message.text == 'Перезагрузить ПК!':
            bot.send_message(message.chat.id, 'Происходит перезагрузка ПК! Ожидайте в течении 1 минуту!')
            restart_system()
        elif message.text == 'Курс Рубля₽.':

            bot.send_message(message.chat.id, 'Ловите свежий курс Рубля! И будьте всегда вкурсе валют, вместе со мной<3')
            bot.send_message(message.chat.id,pybl_price())
            bot.send_message(message.chat.id,'Источник Google.com')

        elif message.text == 'Курс Доллара$.':
            bot.send_message(message.chat.id, 'Ловите свежий курс Доллара! И будьте всегда в курсе валют, вместе со мной<3')
            bot.send_message(message.chat.id,get_currency_price())
            bot.send_message(message.chat.id, 'Источник Google.com')

        elif message.text == 'Курс Евро€.':
            bot.send_message(message.chat.id, 'Ловите свежий курс Евро! И будьте всегда в курсе валют, вместе со мной<3')
            bot.send_message(message.chat.id,euro_price())
            bot.send_message(message.chat.id, 'Источник Google.com')


        elif message.text == 'Открой мне Arizona':
            bot.send_message(message.chat.id, 'Сделано! Приятной игры! И всегда будьте спокойны<3')
            open_ariona() 

        else:
            bot.send_message(message.chat.id,'Я вас не понял, может вы имели, что-то другое.')


# Запускаем вечный цикл, дабы бот работал всё время без остановки.
bot.polling(none_stop = True)


