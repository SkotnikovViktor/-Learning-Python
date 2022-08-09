import json
from pprint import pprint
with open('file.json','r') as file:
    save_file = json.load(file)
pprint(save_file)

