

import numpy as np
import matplotlib.pyplot as plt
import random


if __name__ == '__main__':
    ones = np.ones(30, dtype=np.uint8)
    print(ones)

    doubled = [x * 2 for x in ones]

    doubled = ones * 2
    print(doubled)

    negatives = ones - doubled
    print(negatives)

    y = np.random.rand(30)
    y *= 20
    print(y)

    x = range(0, 30)
    print(x)

    plt.plot(x, y, 'r')
    plt.xlabel("nombre de personnes")
    plt.ylabel("une information associée")
    plt.title("ma graphe")
    plt.savefig("mafig.png")
    plt.show()
