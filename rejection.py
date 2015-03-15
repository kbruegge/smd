# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from scipy.stats import norm

N = 650
x = (np.random.random(N) - 0.5)*8
y = np.random.random(N)*0.6
range = np.arange(-4, 4, 0.001)
plt.plot(range,  norm.pdf(range, 0, 1), label="Standardnormalverteilung", color='orange', linewidth=1.7)

#keep the good ones
mask = y < norm.pdf(x,0,1)
plt.plot(x[mask], y[mask], 'bo')
#rejected ones in light grey
mask = ~mask
plt.plot(x[mask], y[mask], 'o', color='0.85')
plt.legend(loc='best', fancybox=True, framealpha=0.5)
# plt.show()
plt.savefig('rejection.png')
