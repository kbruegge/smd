__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.patches import Ellipse

def main():
    N = 1000000
    mean = (4, 2)
    cov = [[3.5**2, 4.2],[4.2, 1.5**2]]

    d =  np.random.multivariate_normal(mean, cov, N)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    h, ye, xe, misc = ax.hist2d(d[:,0], d[:,1], bins=100)

    e = Ellipse(xy=(4, 2), width=4, height=2, angle=20)
    ax.add_artist(e)

    plt.show()


if __name__ == '__main__':
    main()