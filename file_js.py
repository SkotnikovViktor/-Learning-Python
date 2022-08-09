import json
with open('file.json','r') as file:
    save_file = json.load(file)
print(save_file)