__author__ = 'mackaiver'

import matplotlib.pyplot as plt
import numpy as np


def main():
    #f(x)= 2/3 for all x
    #f = lambda x: (x**3 + 1.0/3.0) - (x**3 - 1.0/3.0)
    fig, [top, bottom] = plt.subplots(nrows=2, ncols=1)

    print("f(x) ist genau im Rahmen der Maschinengenauigkeit")
    g = lambda x: ((3 + (x**3) / 3.0) - (3 - (x**3) / 3.0)) / (x**3)

    xs = np.linspace(-0.0001, 0.0001, 1500)
    #bad stuff happens near zero
    top.plot(xs, g(xs) - 2.0/3.0, color='0.4', label="g(x) - 2/3")
    top.set_title("Abweichung vom exakten Resultat")
    top.legend()

    xs = np.linspace(0.000001, 0.0001, 1500)
    bottom.set_xscale('log')
    bottom.plot(xs, g(xs) - 2.0/3.0, color="0.6")

    fig.show()


if __name__ == '__main__':
    main()
