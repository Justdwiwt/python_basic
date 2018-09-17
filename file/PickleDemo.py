# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import json

data = {'num': 1234, 'name': 'ace'}
json_str = json.dumps(data)
print('python data:', data)
print('json object:', json_str)
data2 = json.loads(json_str)
print('data2["name"]:', data2['name'])
print('data2["num"]:', data2['num'])
with open('dump.txt', 'w')as f:
    json.dump(data, f)
with open('dump.txt', 'r')as f:
    data = json.load(f)
