from os import startfile
import time
import requests
from bs4 import BeautifulSoup
from tkinter import *
from pyautogui import *



def apps():
	window = Tk()
	def show_message():
		label["text"] = key.get()
		f = open('token.txt','w')
		f.write(label["text"])
		f.close()
		itog = Label(text='Ваш ключ был успешно сохранён, пожалуйста закройте программу и перезапустите компьютер для начала работы!')
		itog.pack()
		f1 = open('false.txt','w')
		f1.write('1')
		f1.close()
	number_one = Label(text = 'Приветствуем вас в приложение по активации программы!')
	number_one.pack()
	number_two = Label(text = 'Для того, что-бы программа заработала и вы могли управлять компьютером, вам нужно\nсоздать бота в Telegram.')
	number_two.pack()
	number_tri = Label(text = 'Что-бы создать бота посмотрите данное видео.\n Видео по созданию бота, смотреть ниже.')
	number_tri.pack()
	number_four = Label(text = 'https://youtu.be/W9uGtPhneq')
	number_four.pack()
	key = Entry()
	key.pack()
	but = Button(text='Ввести ключ.',command=show_message)
	but.pack()
	label = Label()
	window.title('Аундефикатор бота')
	window.geometry('650x800+700+200')
	window.resizable(width=False, height=False)
	window.mainloop()



# Запускаем Радмир Лаунчер
def open_radmir():
	startfile("C:/Program Files (x86)/RADMIR LAUNCHER/RADMIR_LAUNCHER_EX.exe")


# Выключение ПК!
def shutdown():
	system("shutdown -s")

			
# Открытие прложения PyCharm с помощью чата в ТГ боте!
def open_PyCharm():
	startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2022.3.3/bin/pycharm64.exe")

# Открытие приложения SublimeText с помощью чата в ТГ боте!
def open_SublimeText():
	startfile("C:/Program Files/Sublime Text/sublime_text.exe")

# Открываем Браузер(Yandex) через бота в ТГ канале!
def open_Yandex():
	startfile("C:/Users/skotn/AppData/Local/Yandex/YandexBrowser/Application/browser.exe")


def open_ariona():
	startfile("C:/Program Files/Arizona Games Launcher/Arizona Games Launcher.exe")

# Делаем Перезагрузку ПК!
def restart_system():
	system("shutdown -r")

# Ввод ПК с спящий режим!
def sleep_system():
	system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# Код для получения курса доллара
# Ссылка на нужную страницу
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
# Заголовки для передачи вместе с URL
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# Метод для получения курса валюты(Доллар)
def get_currency_price():
    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    a = convert[0].text
    return a





# Код для получения курса Евро
# Ссылка на нужную страницу
EURO_RUB = 'https://www.google.com/search?q=курс+евро&sxsrf=APwXEdej-yqbXYX5bInZlpuWoaGJszvpFA%3A1685298323382&source=hp&ei=k5xzZP-LFfvYxc8PgqiO4A0&iflsig=AOEireoAAAAAZHOqoyQbiDhkF_to2Q3OsRbnqWDuJo7O&ved=0ahUKEwi_oZ2_0Zj_AhV7bPEDHQKUA9wQ4dUDCAk&uact=5&oq=курс+евро&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjEIoFECcyCggAEIoFELEDEEMyCggAEIoFELEDEEMyCggAEIoFELEDEEMyBwgAEIoFEEMyBwgAEIoFEEMyCggAEIoFELEDEEMyBwgAEIoFEEMyBQgAEIAEMgcIABCKBRBDOgcIIxDqAhAnOgwIIxCKBRAnEEYQggJQnEdYglRgq1VoAnAAeACAAaoBiAHWB5IBAzQuNZgBAKABAbABCg&sclient=gws-wiz'
# Заголовки для передачи вместе с URL
headers_two = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# Метод для получения курса валюты(Евро)
def euro_price():
    # Парсим всю страницу
    full_page = requests.get(EURO_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": "2"})
    a = convert[0].text
    return a





# Даём ссылку на адрес для парсинга сайта
RYBL_RUB = 'https://www.google.com/search?q=Курс+рубля+&sxsrf=APwXEdcyV9lDZDxCnZAayJCfuLAMQ8G79A%3A1685452312635&source=hp&ei=GPZ1ZKyHJKCPxc8Ppemu4AY&iflsig=AOEireoAAAAAZHYEKDpd3Ug8qa5f-4FVaVc466eAzeG4&ved=0ahUKEwis84KTj53_AhWgR_EDHaW0C2wQ4dUDCAk&uact=5&oq=Курс+рубля+&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjEIoFECcyBwgjEIoFECcyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoLCAAQgAQQsQMQgwE6DAgjEIoFECcQRhCCAjoLCAAQigUQsQMQgwFQyRxY6i5g7y5oAnAAeACAAaEBiAGeB5IBAzcuMpgBAKABAbABCg&sclient=gws-wiz'
# Заголовки для передачи вместе с URL
headers_two = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def pybl_price():
    # Парсим всю страницу
    full_page = requests.get(RYBL_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": "3"})
    a = convert[0].text
    return a


def screen():
	screens = screenshot('screenshot.png')
	return screens



# Не бейте палками и не закидывайте помидорами ПЖ ПЖ ПЖ! Я знаю про переменные но мне лень их исправлять







