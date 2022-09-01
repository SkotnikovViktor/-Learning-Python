# Импорт библиотеки json
import json

# Открытие файла для запись в переменную
with open('Sposob2.json', 'r') as file:
    # Сохранение файла в переменную
    json_data = json.load(file)

json_data = str(json_data)


json = ''

# Цикл for
for i in json_data:
    json += i
    
    if json == "{":
        skobka = "{"
        print('',skobka)
        if json == '"':
            kov = '"'
            print('',kov)
        else:
            print('No')


#{
#    "asd":True} 


# 1 шаг: Проверка на символ "{" 
# 2 шаг: То сохраняем в переменную json 
# 3 шаг: Добавить в переменную json символ переноса на другую строку(гугл что это за символ) 
# 4 шаг: Добавить в переменную json 4 пробела(или Tab)

# Перед каждой строчкой кода писать коментарий (что эта строка делает)









