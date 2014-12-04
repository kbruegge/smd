__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def normal(x, y, mean, covariance_matrix):
    sigma_x = np.sqrt(covariance_matrix[0,0])
    sigma_y = np.sqrt(covariance_matrix[1,1])
    mean_x = mean[0]
    mean_y = mean[1]
    cor = covariance_matrix[1,0]/(sigma_y*sigma_x)
    print("Korrelationskoeffizent: ", cor)
    alpha = 1/(2*np.pi*sigma_x*sigma_y* np.sqrt(1-cor**2))
    exponent = (x-mean_x)**2/(sigma_x**2) + (y-mean_y)**2/(sigma_y**2) - (2*cor*(y-mean_y)*(x-mean_x))/(sigma_x*sigma_y)
    return alpha*np.exp(-0.5*(1/(1-cor**2))*exponent)


def main():
    #plotting limits
    limit_x = -6
    limit_y = 12

    #create meshgrid for plotting function
    x = np.linspace(limit_x, limit_y, 50)
    y = np.linspace(limit_x, limit_y, 50)
    X, Y = np.meshgrid(x, y)

    #values from assignment
    sigma_x = 3.5
    sigma_y = 1.5
    mean_x = 4
    mean_y = 2
    mean = [mean_x, mean_y]
    covariance = 4.2
    #build covariance matrix
    covariance_matrix = np.array([[sigma_x**2, covariance],[covariance, sigma_y**2]])
    #get distribution
    Z = normal(X, Y, mean, covariance_matrix)

    fig, top = plt.subplots(nrows=1, ncols=1)
    top.pcolormesh(X, Y, Z, shading='gouraud')

    #diagonlize covariance matrix
    (v_x,v_y),  v = np.linalg.eig(covariance_matrix)

    #components of first eigenvector
    angle = np.arctan(v[1,0]/v[0,0])
    print("Winkel zur x-Achse: ", np.rad2deg(angle))

    #eigen values are the sigmas
    width = np.sqrt(v_x)*2
    length = np.sqrt(v_y)*2

    print("Ellipsen größen width, length: ", width, length)
    e = Ellipse(xy=(mean_x, mean_y), width=width, height=length, angle= np.rad2deg(angle))
    e.set_color("white")
    e.set_alpha(0.7)
    top.add_artist(e)


    length_x = 0.5*width*np.cos(angle)
    y_2 = mean_y + np.tan(angle)*length_x
    x_2 = mean_x +length_x
    top.plot([mean_x, x_2],[mean_y, y_2] , color='white', linewidth=2)



    angle = np.pi/2 + angle
    length_x = 0.5*length*np.cos(angle)
    y_2 = mean_y + np.tan(angle)*length_x
    x_2 = mean_x + length_x
    top.plot([mean_x, x_2],[mean_y, y_2] , color='white', linewidth=2)



    #draw points
    top.errorbar([mean_x], [mean_y], xerr=sigma_x, yerr=sigma_y, linestyle='o', color="white", ecolor='white')
    top.text(mean_x + 1.5, mean_y - 1.5, r'$(\mu_x + \sigma_y, \mu_y + \sigma_y)$', fontsize=12, color="white")
    plt.title("2D- Gaußverteilung")
    plt.show()




if __name__ == '__main__':
    main()