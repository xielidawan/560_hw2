import json

with open('file1.json', 'r') as f:
    num_list = json.loads(f.read())

pair_dic = {}
for i in num_list:
    pair_dic[i] = 3 * i + 6

with open('file2.json','w') as f:
    f.write(json.dumps(pair_dic))
