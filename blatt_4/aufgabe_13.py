__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def linear_congruential(a = 1601, b = 3456, m = 10000, start = 0,  size = 10000):
    x = np.zeros(size)
    for i in range(1, size):
        x[i] = ((a * x[i-1] + b) % m)

    return x/m

def main():
    print("zufalhhhd")
    a = linear_congruential()
    fig, top = plt.subplots(nrows=1, ncols=1)
    top.set_title("Histogram der Zufallszahlen")
    top.hist(a, bins=100)
    print(a)
    print(np.shape(a))



    fig = plt.figure(2)
    ax = fig.add_subplot(211, projection='3d')
    ax.scatter(a, np.roll(a, 1))
    ax2 = fig.add_subplot(212, projection="3d")
    ax2.scatter(a, np.roll(a,1), np.roll(a, 2))

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
