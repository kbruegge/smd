__author__ = 'mackaiver'

import matplotlib.pyplot as plt
import numpy as np


def main():
    #f(x)= 2/3 for all x
    f = lambda x: (x**3 + 1.0/3.0) - (x**3 - 1.0/3.0)
    fig, [top, center,  bottom] = plt.subplots(nrows=3, ncols=1)

    g = lambda x: ((3 + (x**3) / 3.0) - (3 - (x**3) / 3.0)) / (x**3)

    xs = np.linspace(-0.0001, 0.0001, 1500)

    top.plot(xs, g(xs), color='0.4', label="g(x) ")
    top.plot(xs, f(xs), color='blue', label="f(x)")
    top.set_title("Abweichung vom exakten Resultat")
    top.legend()

    xs = np.linspace(0.000001, 0.0001, 1500)
    center.set_xscale('log')
    center.plot(xs, g(xs), color="0.6", label="g(x)")

    xfs = np.linspace(1, 2**128, 1200)
    bottom.set_xscale('log')
    bottom.plot(xfs, f(xfs), color='blue', label="f(x)")

    plt.show()

if __name__ == '__main__':
    main()
