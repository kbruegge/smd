__author__ = 'awesome bitches'

import numpy as np
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
    pass



def main():
    print("SMD Abgabe 1 von M.B und K.B \n")

    print("\nAufgabe 2")
    aufgabe_2()
    print("\nAufgabe 3")
    aufgabe_3()


if __name__ == '__main__':
    main()