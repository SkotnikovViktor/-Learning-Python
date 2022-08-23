# Импорт библиотеки json
import json
# Открытие файла
with open('file.json', 'r') as file:
    # Сохранение в переменную
    json_data = json.load(file)
for one,two in json_data.items():
    print(one,':',two)
