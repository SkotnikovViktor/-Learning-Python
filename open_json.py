import json
import pprint

with open('file.json', 'r') as f:
    json_data = json.load(f)
    pprint(json_data)