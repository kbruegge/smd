__author__ = 'awesome bitches'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import random
import math


def aufgabe_2():
    filename = "liste.txt"
    names = np.genfromtxt(filename, dtype=np.str)
    firstname, lastname = random.choice(names)
    print("     Zufälliger Name: ", firstname, lastname)


def aufgabe_3():
    print("     Exakter Grenzwert: -1/6 ")
    print("     Berechnete Werte: ")
    for i in range(1, 21):
        x = 1*(10**(-i))
        f = (math.sqrt(9-x) - 3)/x
        print("     ", f)


def aufgabe_4():
    steps = 50

    xs = np.linspace(0.9, 1.1, num=steps)

    a = lambda x: (1-x)**6
    b = lambda x: x**6 - 6*(x**5) + 15*x**4 - 20*x**3 + 15*x**2 - 6*x + 1
    c = lambda x: x*(x*(x*(x*((x - 6)*x + 15) - 20) + 15) - 6) + 1

    fig, (top, bottom) = plt.subplots(nrows=2, ncols=1)
    top.plot(xs, a(xs), color='red', label="Direkte Auswertung")
    top.plot(xs, b(xs), color='blue', label="Ausmultiplizieren")
    top.plot(xs, c(xs), color='green', label="Horner Schema")
    top.set_ylabel('$f(x) = (1-x)^6$')
    top.set_xlabel('$x$')

    #jetzt auf kleinerem bereich
    xs = np.linspace(0.9990001, 1.001, num=steps)
    bottom.plot(xs, a(xs), color='red')
    bottom.plot(xs, b(xs), color='blue')
    bottom.plot(xs, c(xs), color='green')
    bottom.set_ylabel('$f(x) = (1-x)^6$')
    bottom.set_xlabel('$x$')

    #style für die label
    top.ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    bottom.get_yaxis().set_label_coords(-0.1, 0.5)
    top.get_yaxis().set_label_coords(-0.1, 0.5)
    handles, labels = top.get_legend_handles_labels()
    fig.legend(handles, labels, bbox_to_anchor=[1.01, 0.97], ncol=1, borderaxespad=1.25)
    fig.suptitle('Polynom Auswertungen', fontsize=14, fontweight='bold')
    #top.title("my title", y=0.6)


def main():
    print("SMD Abgabe 1 von M.B und K.B \n")

    print("\nAufgabe 2")
    aufgabe_2()
    print("\nAufgabe 3")
    aufgabe_3()
    print("\nAufgabe 4")
    aufgabe_4()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()