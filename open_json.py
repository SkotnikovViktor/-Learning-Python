# Импорт библиотеки json
import json
# Открытие файла для запись в переменную
with open('file.json', 'r') as file:
    # Сохранение файла в переменную
    json_data = json.load(file)
    # Цикл for
for one,two in json_data.items():
    print(one,':',two,',')

