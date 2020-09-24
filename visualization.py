import matplotlib.pyplot as plt
import json
def run():
    with open('file1.json', 'r') as f:
        x = json.loads(f.read())
    with open('file2.json', 'r') as f:
        y = json.loads(f.read())

    # scatter
    # plt.scatter(x, y, marker='*')

    # linear
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.savefig('file3.jpg')
    plt.show()

if __name__ == '__main__':
    run()
