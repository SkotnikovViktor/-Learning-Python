# Импорт библиотеки json
import json
# Открытие файла
with open('file.json', 'r') as f:
    # Сохранение в переменную
    json_data = json.load(f)
for one,two in json_data.items():
    print(one,':',two)