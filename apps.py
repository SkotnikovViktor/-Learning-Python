from tkinter import *
import getpass
import os
from pathlib import Path
from ctypes import *
import ctypes
import subprocess
import sys
import webbrowser
import time

#if not ctypes.windll.shell32.IsUserAnAdmin():
#    print("not an admin, restarting...")
#    subprocess.run(["launcher.exe", sys.executable, *sys.argv])
#else:
#    print("I'm an admin now.")



def appsing():
    window = Tk()
    def show_message():
        label["text"] = key.get()
        f = open('token.txt','w')
        f.write(label["text"])
        f.close()
        f1 = open('false.txt','w')
        f1.write('1')
        f1.close()
        itog = Label(text='Ваш ключ был успешно сохранён\n пожалуйста закройте программу и перезапустите компьютер для начала работы!')
        itog.pack()
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
    window.geometry('900x500')  
    window.resizable(width=True, height=True)
    window.mainloop()
appsing()
