# Этот код пербирает текстовый файл с матами
# в файл формата json
# для последующей его обработки ботом.

import json

ar = []

with open('cenz.txt', 'r', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            print(n)
            ar.append(n)

print(ar)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e, ensure_ascii=False)

y = json.dumps(ar)
print('tr')
print(ar)
