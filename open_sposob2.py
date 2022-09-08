# Делаем импорт библиотеки 
import json

# Открытие файла 
with open('Sposob2.json', 'r') as file:
    # Запись файла в перемнную
    json_data = json.load(file)

# Делаем из типа данных json тип данных str
json_data = str(json_data)

# Создаем переменную json
json = ''

# Начинаем цикл for 
for i in json_data:
    # Присваиваем переменной json переменную i (что-бы все символы были вместе)

    
    if i == '{':
        json = json + i + '\n'


print(json)






