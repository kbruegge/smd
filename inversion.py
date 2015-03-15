# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
# from scipy.stats import norm

N =50000
# x = (np.random.random(N) - 0.5)*8
# y = np.random.random(N)*0.6
range = np.arange(0, np.pi, 0.01)
plt.plot(range,  np.sin(range)*0.5, label="$sin(x) \cdot 0.5$", color='orange', linewidth=1.7)

inv = np.arccos(1 - 2 * np.random.random(N))
# print(inv)
plt.hist(inv, histtype='step', bins = 50, normed=True, color="blue", label="Histogram für $F^{-1}(x)$  mit "+str(N)+" Einträgen")
plt.legend(loc='best', fancybox=True, framealpha=0.5)
# plt.show()
plt.savefig('inversion.png')
