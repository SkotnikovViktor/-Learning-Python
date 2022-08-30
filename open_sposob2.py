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
    
    if json == '{':
        skobka = '{'
        print('',skobka)
    elif json == "'":
        kov = "'"
        print('     ',kov)
        







