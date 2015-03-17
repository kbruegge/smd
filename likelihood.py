# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

r = np.arange(0,20,0.1)
#ableitung
F = 1/(np.math.factorial(9)*np.math.factorial(8)*np.math.factorial(13))* np.exp(-3 * r)*r**(29)*(30-3*r)
#likelihood
L = 1/(np.math.factorial(9)*np.math.factorial(8)*np.math.factorial(13))* r**(30) *np.exp(-3*r)

l = -3 * r + 30*np.log(r) - (np.log(np.math.factorial(8)) + np.log(np.math.factorial(9)) + np.log(np.math.factorial(13)))
f = -3 + 30/r


fig, (top, bottom) = plt.subplots(nrows=2, ncols=1)
fig.suptitle("Likelihood einer Poisson Verteilung")

top.plot(r,L, color='blue', label="Likelihood")
top.plot(r,F, color='orange', label="Ableitung der Likelihood")
top.legend(loc='best', fancybox=True, framealpha=0.5)

bottom.plot(r,l, color='blue', label="LogLikelihood")
bottom.plot(r,f, color='orange', label="Ableitung der LogLikelihood")
bottom.legend(loc='best', fancybox=True, framealpha=0.5)

plt.xlabel("$\lambda$")
plt.xlim(xmax=20, xmin=0)
plt.ylim(ymax=10, ymin=-10)

# plt.show()
plt.savefig('likelihood.png')
