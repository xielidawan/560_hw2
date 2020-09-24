import random
import json


def run():
    num_list = []
    for i in range(1000):
        num_list.append(random.randint(0, 100))

    with open('file1.json', 'w') as f:
        f.write(json.dumps(num_list))

if __name__ == '__main__':
    run()