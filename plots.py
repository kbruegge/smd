# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

x_1 = np.random.random(15000)
x_2 = np.random.random(15000)
plt.hist(x_1, bins=20, histtype="step",  linewidth=1.2, label="Gleichverteilung aus $[0, 1)$ mit 15000 Einträgen")
plt.hist(x_2, bins=20, histtype="step",  linewidth=1.2, label="Gleichverteilung aus $[0, 1)$ mit 15000 Einträgen")

s = x_1 + x_2 - 0.5
plt.hist(s, bins=20, histtype="step", linewidth=1.5, label="Summe der Verteilungen um  -0.5 verschoben ")
plt.legend(loc='best', fancybox=True, framealpha=0.5)
plt.savefig('verteilung_1.png')
