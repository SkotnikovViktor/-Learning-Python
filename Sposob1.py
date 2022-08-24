import json
with open('main_file_json.json','r') as file:
    save_file = json.load(file)
print(json.dumps(save_file,sort_keys = True, indent = 4))


