# coding: utf-8

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
# from scipy.stats import chi2

N = 1000
cov = np.array([[1,0.5],[0.5,4]])
mean = np.array([0,0])
a = np.random.multivariate_normal(mean, cov, size=N)

c = (1/(N - 1)) * np.dot(a.T, a)
# print(np.shape(c))
lambdas, V = np.linalg.eigh(c)
plt.scatter(a[:, 0], a[:,1])
# plt.arrow(0, 0, V[1,0], V[1,1], head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, lambdas[0]*V[0,0], lambdas[0]*V[1,0], linewidth=1.4, color='orange',  head_width=0.1)
arrow = plt.arrow(0, 0, lambdas[1]*V[0,1], lambdas[1]*V[1,1], linewidth=1.4, color='orange',  head_width=0.1)
# print(lambdas, V)
# class_1 = X[Y == 1]
# class_2 = X[Y < 1]
#
# mu_1 = np.mean(class_1, axis=0)
# mu_2 = np.mean(class_2, axis=0)
#
# variance_1 = np.dot((class_1 - mu_1).T, (class_1 - mu_1))
# variance_2 = np.dot((class_2 - mu_2).T, (class_2 - mu_2))
#
# weights =np.dot( np.linalg.inv(variance_1 + variance_2)  ,  (mu_2 - mu_1))
#
# c = np.dot(weights , (mu_1 + mu_2)) * 0.5

plt.title("Hauptkomponenten")
# plt.axvline(c, linewidth=1.3, color='0.5', label="Schwellwert $c$")
# plt.hist(np.dot(class_1, weights), linewidth=1.5, histtype='step', bins = 10, normed=True, color="orange", label="Projektion Klasse 1")
# plt.hist(np.dot(class_2, weights), linewidth=1.5, histtype='step', bins = 10, normed=True, color="blue", label="Projektion Klasse 2")
plt.legend([arrow,], ['Hauptkomponente',],loc='best', fancybox=True, framealpha=0.5)
# plt.legend()

plt.xlim(xmax = 7, xmin=-7)
plt.ylim(ymax = 7, ymin=-7)
# plt.show()

plt.savefig('pca.png')
