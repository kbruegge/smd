__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.patches import Ellipse

def normal(x, y, mu_x, mu_y, sigma_x, sigma_y):
    cov = 4.2
    alpha = 1/(2*np.pi*np.sqrt((sigma_x**2*sigma_y**2 - cov**2)))
    cor = 0.8
    exponent = (x-mu_x)**2/(sigma_x**2) + (y-mu_y)**2/(sigma_y**2) - (2*cor*(y-mu_y)*(x-mu_x))/(sigma_x*sigma_y)
    return alpha*np.exp(-0.5*(1/(1-cor**2))*exponent)


def main():

    x = np.linspace(-5, 10, 50)
    y = np.linspace(-5, 10, 50)
    X, Y = np.meshgrid(x, y)
    Z = normal(X, Y, 4, 2, 3.5, 1.5)

    fig, ax = plt.subplots(nrows=1, ncols=1)
    t = ax.pcolormesh(X, Y, Z, shading='gouraud')
    #fig.colorbar(t, ax=ax)

    # d =  np.random.multivariate_normal(mean, cov, N)
    # h, ye, xe, misc = ax.hist2d(d[:,0], d[:,1], bins=100)

    angle = 20
    e = Ellipse(xy=(4, 2), width=3.5, height=1.5, angle=angle)
    e.set_color("white")
    e.set_alpha(0.8)
    ax.add_artist(e)

    #draw a line
    x= [4,10]
    y= [2, np.arctan(angle)*4]
    plt.plot(x, y, color="white", linewidth=2)
    plt.show()

#     from pylab import *
#
#
# Z = (1 - X/2. + X**5 + Y**3) * exp(-X**2 - Y**2) # calcul du tableau des valeurs de Z
#
# pcolormesh(X, Y, Z, shading='gouraud')
# colorbar()
#
# show()


if __name__ == '__main__':
    main()