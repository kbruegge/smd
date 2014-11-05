__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt

def f(theta, E):
    alpha   = 1/137
    m       = 0.511 # GeV
    gamma   = E/m
    beta    = np.sqrt(1- 1/(gamma**2))
    #print("E: " + str(E) + "beta: " + str(beta))
    s       = (2*E)**2
    denominator = (1 - beta**2 * np.cos(theta)**2 )
    dq      = alpha**2/s * ( (2 + np.sin(theta)**2)/denominator - ((2*np.sin(theta)**4)/(denominator**2)))
    return dq

def kond(x):
    return 1/2 *  abs((x*(1.99994778261853 * np.cos(2*x) - 2.000156668509471) * np.sin(2* x))/((0.9999477744360000 * np.cos(x)**2 - 1)**3 * ((np.sin(x)**2+2)/(1-0.9999477744360000 * np.cos(x)**2)-(2 *np.sin(x)**4)/(1-0.9999477744360000 *np.cos(x)**2)**2)))

def main():
    fig, [top,  bottom] = plt.subplots(nrows=2, ncols=1)

    ts = np.linspace(0, 0.0000001 , 1000)
    for e in range(10, 100, 10):
        top.plot(ts, f(ts, e))
    top.set_ylabel("Wirkungsquerschnitt")


    ts = np.linspace(0, np.pi + 0.00001, 1000)
    bottom.set_ylim(0, 10)
    bottom.plot(ts, kond(ts))
    bottom.set_ylabel("Konditionszahl")
    plt.show()



if __name__ == '__main__':
    main()
