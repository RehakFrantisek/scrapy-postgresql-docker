import json

f = open('./srealityscraper/sreality.json')

data = json.load(f)
insertfile = open('create_table.sql', 'a', encoding='utf-8')

for i, x in enumerate(data):
    if i < len(data) - 1:
        insertfile.write('(\'' + x['title'] + '\',\'' + x['image_url'] + '\'),\n')
    else:
        insertfile.write('(\'' + x['title'] + '\',\'' + x['image_url'] + '\');\n')

insertfile.close()
f.close()
