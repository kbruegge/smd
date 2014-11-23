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
    sigma_x = 3.5
    sigma_y = 3.4
    cor = 0.8
    covariance = 0.1
    Z = normal(X, Y, 4, 2, sigma_x, sigma_y)

    fig, ax = plt.subplots(nrows=1, ncols=1)
    t = ax.pcolormesh(X, Y, Z, shading='gouraud')
    #fig.colorbar(t, ax=ax)

    # d =  np.random.multivariate_normal(mean, cov, N)
    # h, ye, xe, misc = ax.hist2d(d[:,0], d[:,1], bins=100)


    angle = 0.5 * np.arctan(2* cor * sigma_x * sigma_y/(sigma_x**2 - sigma_y**2))
    cov = [[sigma_x**2, covariance], [covariance, sigma_y**2]]
    rot = [[np.cos(angle), np.sin(angle) ], [-np.sin(angle), np.cos(angle)]]

    matrix = np.dot(np.transpose(rot), np.dot(cov, rot))

    print("MATRIX: ", matrix)

    w, v = np.linalg.eig(cov)
    matrix = np.dot(np.transpose(v), np.dot(cov, v))

    print("NEUE AMTRIDJFSDAM: ", matrix)



    e = Ellipse(xy=(4, 2), width=matrix[0,0], height= matrix[1,1], angle= np.rad2deg(angle))
    e.set_color("white")
    e.set_alpha(0.8)
    ax.add_artist(e)

    #draw a line
    x= [4,10]
    y= [2, 2 + np.tan(angle)*6]
    plt.plot(x, y, color="white", linewidth=2)
    plt.show()




if __name__ == '__main__':
    main()