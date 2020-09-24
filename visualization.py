import matplotlib.pyplot as plt
import json

with open('file2.json', 'r') as f:
    pair_dict = json.loads(f.read())

x = []
y = []
for (i, j) in pair_dict.items():
    x.append(int(i))
    y.append(int(j))

# scatter
# plt.scatter(x, y, marker='*')

# linear
fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig('file3.jpg')
plt.show()
