
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    
    # generate vector of length 30, filled with 1
    v1 = [1 for _ in range(30)]

    v1 = np.ones(30, dtype=int) #[1, 1, 1, ...]
    v2 = np.ones(30, dtype=int) * 2 #[2, 2, 2, 2, 2 ...]

    x = list(range(30))
    y = v1 * np.random.rand(30) * 10

    plt.plot(x, y, 'b')
    plt.xlabel("nombre de personnes")
    plt.ylabel("une information associée")
    plt.title(f"Pop:{v2[0]}, LR:{v1[1]}")
    plt.savefig("myfig.png")
    plt.show()

