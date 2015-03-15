# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
# from scipy.stats import chi2
from sklearn.datasets import make_classification


X, Y = make_classification(n_samples=7000, n_features=10, n_redundant=0, n_informative=4,
                             n_clusters_per_class=1)

# N =50000
# x = (np.random.random(N) - 0.5)*8
# y = np.random.random(N)*0.6
class_1 = X[Y == 1]
class_2 = X[Y < 1]

mu_1 = np.mean(class_1, axis=0)
mu_2 = np.mean(class_2, axis=0)

variance_1 = np.dot((class_1 - mu_1).T, (class_1 - mu_1))
variance_2 = np.dot((class_2 - mu_2).T, (class_2 - mu_2))

weights =np.dot( np.linalg.inv(variance_1 + variance_2)  ,  (mu_2 - mu_1))

c = np.dot(weights , (mu_1 + mu_2)) * 0.5

plt.title("Projektion nach Fisher Diskriminanz")
plt.axvline(c, linewidth=1.3, color='0.5', label="Schwellwert $c$")
plt.hist(np.dot(class_1, weights), linewidth=1.5, histtype='step', bins = 10, normed=True, color="orange", label="Projektion Klasse 1")
plt.hist(np.dot(class_2, weights), linewidth=1.5, histtype='step', bins = 10, normed=True, color="blue", label="Projektion Klasse 2")
plt.legend(loc='best', fancybox=True, framealpha=0.5)


# plt.xlim(xmax = 10)
# plt.show()

plt.savefig('fisher.png')
