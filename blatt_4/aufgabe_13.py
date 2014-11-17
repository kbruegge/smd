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
    a = linear_congruential()




    fig = plt.figure(figsize=(10, 9))

    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.set_title("Linear Congruential")
    ax1.scatter(a, np.roll(a, 1))

    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.set_title("Linear Congruential")
    ax2.scatter(a, np.roll(a,1), np.roll(a, 2))

    a = np.random.random(10000)
    ax1 = fig.add_subplot(2, 2, 3, projection='3d')
    ax1.set_title("np.random")
    ax1.scatter(a, np.roll(a, 1), color="red")
    ax2 = fig.add_subplot(2, 2, 4, projection='3d')
    ax2.set_title("np.random")
    ax2.scatter(a, np.roll(a,1), np.roll(a, 2), color="red")
    #ax3.scatter(a, np.roll(a, 1) , color="red")
    #ax4.scatter(a, np.roll(a,1), np.roll(a, 2), color="red")

    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()
