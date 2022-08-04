import tkinter as tk
from tkinter import Button
import pygame
import time
import random

pygame.init()
pygame.mixer.init()
window = tk.Tk()
window.geometry('3300x1200')
window.title('SchoolBox ')
#pygame.mixer.music.load('spok.mp3')
#pygame.mixer.music.play()




def A():
    pygame.mixer.music.load('gen-6.mp3')
    pygame.mixer.music.play()
def Б():
    pygame.mixer.music.load('gen-7.mp3')
    pygame.mixer.music.play()
def В():
    pygame.mixer.music.load('gen-8.mp3')
    pygame.mixer.music.play()
def Г():
    pygame.mixer.music.load('gen-9.mp3')
    pygame.mixer.music.play()

def Д():
    pygame.mixer.music.load('gen-10.mp3')
    pygame.mixer.music.play()
def Е():
    pygame.mixer.music.load('gen-11.mp3')
    pygame.mixer.music.play()



def Ё():
    pygame.mixer.music.load('gen-12.mp3')
    pygame.mixer.music.play()

def Ж():
    pygame.mixer.music.load('gen-13.mp3')
    pygame.mixer.music.play()
def З():
    pygame.mixer.music.load('gen-14.mp3')
    pygame.mixer.music.play()
def И():
    pygame.mixer.music.load('gen-15.mp3')
    pygame.mixer.music.play()
def Й():
    pygame.mixer.music.load('gen-16.mp3')
    pygame.mixer.music.play()
def К():
    pygame.mixer.music.load('gen-17.mp3')
    pygame.mixer.music.play()
def Л():
    pygame.mixer.music.load('gen-18.mp3')
    pygame.mixer.music.play()
def М():
    pygame.mixer.music.load('gen-19.mp3')
    pygame.mixer.music.play()
def Н():
    pygame.mixer.music.load('gen-20.mp3')
    pygame.mixer.music.play()

def О():
    pygame.mixer.music.load('gen-21.mp3')
    pygame.mixer.music.play()
def П():
    pygame.mixer.music.load('gen-22.mp3')
    pygame.mixer.music.play()
def Р():
    pygame.mixer.music.load('gen-23.mp3')
    pygame.mixer.music.play()
def С():
    pygame.mixer.music.load('gen-24.mp3')
    pygame.mixer.music.play()
def Т():
    pygame.mixer.music.load('gen-25.mp3')
    pygame.mixer.music.play()
def У():
    pygame.mixer.music.load('gen-26.mp3')
    pygame.mixer.music.play()
def Ф():
    pygame.mixer.music.load('gen-27.mp3')
    pygame.mixer.music.play()
def Х():
    pygame.mixer.music.load('gen-28.mp3')
    pygame.mixer.music.play()
def Ц():
    pygame.mixer.music.load('gen-29.mp3')
    pygame.mixer.music.play()
def Ч():
    pygame.mixer.music.load('gen-30.mp3')
    pygame.mixer.music.play()
def Ш():
    pygame.mixer.music.load('gen-31.mp3')
    pygame.mixer.music.play()
def Щ():
    pygame.mixer.music.load('gen-32.mp3')
    pygame.mixer.music.play()
def Ъ():
    pygame.mixer.music.load('gen-33.mp3')
    pygame.mixer.music.play()
def Ы():
    pygame.mixer.music.load('gen-34.mp3')
    pygame.mixer.music.play()
def Ь():
    pygame.mixer.music.load('gen-35.mp3')
    pygame.mixer.music.play()
def Э():
    pygame.mixer.music.load('gen-36.mp3')
    pygame.mixer.music.play()
def Ю():
    pygame.mixer.music.load('gen-37.mp3')
    pygame.mixer.music.play()
def я():
    pygame.mixer.music.load('gen-38.mp3')
    pygame.mixer.music.play()
def fon():
    pygame.mixer.music.load('Music_fon.mp3')
    pygame.mixer.music.play()
def fon2():
    pygame.mixer.music.load('Music_fon.mp3')
    pygame.mixer.music.stop()

    # pygame.mixer.music.load()
    # pygame.mixer.music.play(0)


btn1 = tk.Button(text = 'Aa', width = 10, height = 5, command = A)
btn2 = tk.Button(text = 'Бб', width = 10, height = 5, command = Б)
btn3 = tk.Button(text = 'Вв', width = 10, height = 5, command = В)
btn4 = tk.Button(text = 'Гг', width = 10, height = 5, command = Г)
btn5 = tk.Button(text = 'Дд', width = 10, height = 5, command = Д)
btn6 = tk.Button(text = 'Ее', width = 10, height = 5, command = Е)
btn7 = tk.Button(text = 'Ёё', width = 10, height = 5, command = Ё)
btn8 = tk.Button(text = 'Жж', width = 10, height = 5, command = Ж)
btn9 = tk.Button(text = 'Зз', width = 10, height = 5, command = З)
btn10 = tk.Button(text = 'Ии', width = 10, height = 5, command = И)
btn11 = tk.Button(text = 'Йй', width = 10, height = 5, command = Й)
btn12 = tk.Button(text = 'Кк', width = 10, height = 5, command = К)
btn13 = tk.Button(text = 'Лл', width = 10, height = 5, command = Л)
btn14 = tk.Button(text = 'Мм', width = 10, height = 5, command = М)
btn15 = tk.Button(text = 'Нн', width = 10, height = 5, command = Н)
btn16 = tk.Button(text = 'Оо', width = 10, height = 5, command = О)
btn17 = tk.Button(text = 'Пп', width = 10, height = 5, command = П)
btn18 = tk.Button(text = 'Рр', width = 10, height = 5, command = Р)
btn19 = tk.Button(text = 'Сс', width = 10, height = 5, command = С)
btn20 = tk.Button(text = 'Тт', width = 10, height = 5, command = Т)
btn21 = tk.Button(text = 'Уу', width = 10, height = 5, command = У)
btn22 = tk.Button(text = 'Фф', width = 10, height = 5, command = Ф)
btn23 = tk.Button(text = 'Хх', width = 10, height = 5, command = Х)
btn24 = tk.Button(text = 'Цц', width = 10, height = 5, command = Ц)
btn25 = tk.Button(text = 'Чч', width = 10, height = 5, command = Ч)
btn26 = tk.Button(text = 'Шш', width = 10, height = 5, command = Ш)
btn27= tk.Button(text = 'Щщ', width = 10, height = 5, command = Щ)
btn28 = tk.Button(text = 'Ъъ', width = 10, height = 5, command = Ъ)
btn29 = tk.Button(text = 'Ыы', width = 10, height = 5, command = Ы)
btn30 = tk.Button(text = 'Ьь', width = 10, height = 5, command = Ь)
btn31 = tk.Button(text = 'Ээ', width = 10, height = 5, command = Э)
btn32 = tk.Button(text = 'Юю', width = 10, height = 5, command = Ю)
btn33 = tk.Button(text = 'Яя', width = 10, height = 5, command = я)
btn_fon = tk.Button(text = 'Вкл', width = 10,height = 5, command=fon )
btn_fon2 = tk.Button(text = 'Выкл', width = 10,height = 5, command=fon2 )


## Рвзмещение цифр
btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row = 0, column = 2)
btn4.grid(row = 0, column = 3)
btn5.grid(row = 0, column = 4)
btn6.grid(row = 0, column = 5)
btn7.grid(row = 0, column = 6)
btn8.grid(row = 0, column = 7)
btn9.grid(row = 0, column = 8)
btn10.grid(row = 0, column = 9)
btn11.grid(row = 0, column = 10)
btn12.grid(row = 1, column = 0)
btn13.grid(row = 1, column = 1)
btn14.grid(row = 1, column = 2)
btn15.grid(row = 1, column = 3)
btn16.grid(row = 1, column = 4)
btn17.grid(row = 1, column = 5)
btn18.grid(row = 1, column = 6)
btn19.grid(row = 1, column = 7)
btn20.grid(row = 1, column = 8)
btn21.grid(row = 1, column = 9)
btn22.grid(row = 1, column = 10)
btn23.grid(row = 2, column = 0)
btn24.grid(row = 2, column = 1)
btn25.grid(row = 2, column = 2)
btn26.grid(row = 2, column = 3)
btn27.grid(row = 2, column = 4)
btn28.grid(row = 2, column = 5)
btn29.grid(row = 2, column = 6 )
btn30.grid(row = 2, column = 7 )
btn31.grid(row = 2, column = 8 )
btn32.grid(row = 2, column = 9 )
btn33.grid(row = 2, column = 10 )
btn_fon.grid(row = 8, column = 12 )
btn_fon2.grid(row = 8, column = 15 )
## number

window.mainloop()
