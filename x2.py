# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from scipy.stats import chi2
# from scipy.stats import norm

N =50000
# x = (np.random.random(N) - 0.5)*8
# y = np.random.random(N)*0.6
r = np.arange(0, 10, 0.01)

n = 4
plt.plot(r,  chi2.pdf(r, n), label="$\chi_"+str(n)+"^2$", color='0.5')

n=3
plt.plot(r,  chi2.pdf(r, n), '--', label="$\chi_"+str(n)+"^2$", color='0.2')

n = 4
inv =  np.log(np.random.random((N, n*0.5)))
inv = -2 * np.sum(inv, axis=1)
plt.hist(inv, linewidth=1.5, histtype='step', bins = 50, normed=True, color="blue", label="Histogram für  $\chi_"+str(n)+"^2$  mit "+str(N)+" Einträgen")


n = 3
invodd =  np.log(np.random.random((N, (n-1)*0.5)))
invodd = -2 * np.sum(invodd, axis=1) + np.random.normal(loc=0, scale=1, size=N)**2
plt.hist(invodd, linewidth=1.5, histtype='step', bins = 50, normed=True, color="orange", label="Histogram für  $\chi_"+str(n)+"^2$  mit "+str(N)+" Einträgen")

plt.legend(loc='best', fancybox=True, framealpha=0.5)
plt.xlim(xmax = 10)
# plt.show()
plt.savefig('x2.png')
