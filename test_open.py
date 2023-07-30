import time
from telebot import *
from os import remove
#from function import *
from datetime import datetime
from datetime import *
from PIL import Image



file = open('false.txt','r')
falsing = file.read()
if str(falsing)=='0':
    print('Всё прошло успешно!')
    print('Вот, что было в файле:'+falsing)
else:
    file_token = open('token.txt','r')
    file_token_bot = file_token.read()
    bot = file_token_bot
    file_token.close() 
file.close()
