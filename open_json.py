# Импорт библиотеки json
import json
# Открытие файла
with open('file.json', 'r') as f:
    # Сохранение в переменную
    json_data = json.load(f)
# Первый пробный код (не работает)
for i,y in json_data:
    print(i[y])
