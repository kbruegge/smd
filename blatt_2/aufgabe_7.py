__author__ = 'mackaiver'

import numpy as np
import matplotlib.pyplot as plt


def bin_data(data, title="Histogram"):
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2)
    ax1.hist(data, color='0.6', bins=5)
    ax1.text(0.85, 0.85, '5 Bins', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes)
    ax2.hist(data, color='0.6', bins=10)
    ax3.hist(data, color='0.6', bins=15)
    ax4.hist(data, color='0.6', bins=20)
    ax5.hist(data, color='0.6', bins=30)
    ax6.hist(data, color='0.6', bins=50)
    ax6.text(0.85, 0.85, '50 Bins', horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes)
    # ax1.set_title("Gewichte gebinnt")
    fig.suptitle(title, fontsize=14, fontweight='bold')
    fig.show()


def main():
    print("Lade Daten..")
    weight, height = np.genfromtxt("Gewicht_Groesse.txt", unpack=True)
    bin_data(weight, title="Gewicht")
    bin_data(height, title="Groesse")
    random_data = np.log10(np.random.randint(1, 100, 100000))
    bin_data(random_data, "Zufalls Zahlen")
    input()






if __name__ == '__main__':
    main()
