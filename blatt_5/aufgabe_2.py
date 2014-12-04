__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.patches import Ellipse

def normal(N = 10000):
    l = np.zeros((N,2))
    for i in range(N):
        mu_x = 4
        sigma_x = 1.5
        x = np.random.normal(mu_x, sigma_x, 1)
        mean = 2+0.35*(x-4)
        sigma = 0.9
        y =np.random.normal(mean, sigma, 1)
        l[i,0] = x
        l[i,1] = y
    return l
def modi(b):
    mean_b = (b[:,0].mean(), b[:,1].mean())
    sigma_b = (b[:,0].std(), b[:,1].std())
    cov_b = np.cov(b[:,0], b[:, 1])
    cor = cov_b[0,1]/(sigma_b[0]* sigma_b[1])
    return mean_b, sigma_b, cov_b, cor

def main():

    fig, (top, center, bottom) = plt.subplots(nrows=3, ncols=1)
    #fig.colorbar(t, ax=ax)
    mean = [0,4]
    cov = [[1.5**2, 0], [0, 1.5**2]]
    N = 50000

    a = np.random.multivariate_normal(mean, cov, N)
    print("Mean, sigma and covariance for distribution A: ", modi(a))


    b = normal(N=N)
    print("Mean, sigma and covariance for distribution B: ", modi(b))


    c = np.append(a, b, axis=0)
    print("Mean, sigma and covariance for total distribution: ", modi(c))



    h, ye, xe, misc = top.hist2d(a[:,0], a[:,1], bins=40)
    fig.colorbar(misc, ax=top)
    h, ye, xe, misc = center.hist2d(b[:,0], b[:,1], bins=40)
    fig.colorbar(misc, ax=center)
    h, ye, xe, misc = bottom.hist2d(c[:,0], c[:,1], bins=40)
    fig.colorbar(misc, ax=bottom)

    plt.show()

if __name__ == '__main__':
    main()