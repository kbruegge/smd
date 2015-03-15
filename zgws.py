# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from scipy.stats import norm

range = np.arange(-10, 10, 0.005)
n = 500
mu = 0.5
sigma = 1/12
bins = 30

x = np.random.random((n, 15000))
s = (np.sum(x, axis=0) - n * mu)
low, high = np.floor(s.min()), np.ceil(s.max())
bins = np.linspace(low, high, high - low + 1)
hist, edges = np.histogram(s, bins=bins, density=True)
# hist, edges = np.histogram(s, bins=bins)
# hist = hist/np.sum(hist)
# plt.hist(s, bins=20, weights=weights,  histtype="step", linewidth=1.5, label="Summe der Verteilungen nach 0 verschoben ")
plt.bar(edges[:-1], hist, width=1)
plt.plot(range,  norm.pdf(range, 0, 2))
plt.legend(loc='best', fancybox=True, framealpha=0.5)
plt.show()
# plt.savefig('zgws.png')
