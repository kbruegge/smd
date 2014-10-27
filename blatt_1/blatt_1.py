__author__ = 'awesome bitches'

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import random
import math

def aufgabe_1():
    #print "Writing a tree and filling a histogram"
    #
    # f = TFile("tree.root", "recreate")
    # t = TTree("name_of_tree", "tree title")
    #
    # # create 1 dimensional float arrays (python's float datatype corresponds to c++ doubles)
    # # as fill variables
    # x = np.zeros(1, dtype=float)
    # y = np.zeros(1, dtype=float)
    # z = np.zeros(1, dtype=float)
    #
    # # create the branches and assign the fill-variables to them
    # t.Branch('x', x, 'uniform/D')
    #
    # # create the histograms
    # hUniform = TH1F("uniform", "uniform", 40, 1, 1001)
    # h2D = TH2F("B", "Bla", 40, 0, 1000, 40, 0, 1000)
    #
    # # create some random numbers, fill them into the fill varibles and call Fill()
    # for i in range(10000):
    #     x[0] = random.randint(1, 1001)
    #     y[0] = random.gauss(x[0], x[0])
    #     t.Fill()
    #     hUniform.Fill( x[0] )
    #     h2D.Fill(x[0], y[0] )


    # write the tree into the output file and close the file
    # f.Write()
    # f.Close()
    print("     ROOT stinkt ganz doll. DIE BAYERN AUCH")



def aufgabe_2():
    filename = "liste.txt"
    names = np.genfromtxt(filename, dtype=np.str)
    firstname, lastname = random.choice(names)
    print "     Zufaelliger Name: ", firstname, lastname


def aufgabe_3():
    print("     Exakter Grenzwert: -1/6 ")
    print("     Berechnete Werte: ")
    for i in range(1, 21):
        x = 1*(10**(-i))
        f = (math.sqrt(9-x) - 3)/x
        print "     ", f


def aufgabe_4():
    steps = 200

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

    #style fuer die label
    top.ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    bottom.get_yaxis().set_label_coords(-0.1, 0.5)
    top.get_yaxis().set_label_coords(-0.1, 0.5)
    handles, labels = top.get_legend_handles_labels()
    fig.legend(handles, labels, bbox_to_anchor=[1.01, 0.97], ncol=1, borderaxespad=1.25)
    fig.suptitle('Polynom Auswertungen', fontsize=14, fontweight='bold')
    #top.title("my title", y=0.6)


def main():
    print("SMD Abgabe 1 von M.B und K.B \n")
    print("\nAufgabe 1")
    aufgabe_1()
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