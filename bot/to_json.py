# Этот код пербирает текстовый файл с матами
# в файл формата json
# для последующей его обработки ботом.

import json

ar = []

with open('cenz.txt', 'r') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('cenz.json', 'w') as e:
    json.dump(ar, e)
