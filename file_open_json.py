import json
with open('file.json','r') as file:
    save_file = json.load(file)
print(json.dumps(save_file,sort_keys = True, indent = 4))


