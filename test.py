import json
import re


with open("data.json") as file:
    data = json.load(file)
tmp = {}

for i in data:
    text = ''.join(x for x in i if ord(x) < 256)
    tmp[text] = {
        'name': data[i]['name'],
        'url': data[i]['url']
    }
with open("data2.json", "w") as f:
    json.dump(tmp, f)
    print("加载入文件完成...")
