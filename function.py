import json

with open('file1.json', 'r') as f:
    num_list = json.loads(f.read())

y = []
for i in num_list:
    y.append(3 * i + 6)

with open('file2.json', 'w') as f:
    f.write(json.dumps(y))
