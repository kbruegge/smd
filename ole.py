# coding: utf-8

# import matplotlib
# matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

N = 300
cov = np.array([[3,0.7],[0.7,1]])
mean = np.array([0,0])

data = np.random.multivariate_normal(mean, cov, size=N)
x_data = data[:,0]
y_data = data[:,1]
# ## baue design matrix
def f1(x):
    return 1

def f2(x):
    return x
#
X = np.zeros((N, 2))

X[:, 0] = f1(None)
X[:, 1] = f2(x_data)

# print(X)
print(np.dot(X.T, X))
M = np.dot( np.linalg.inv( np.dot(X.T, X) ) , X.T)
#print(M)

a = np.dot(M, y_data)
print(a)

plt.title("OLS")
plt.scatter(x_data, y_data, color="blue")
r = np.linspace(-10, 10, 5)
plt.plot(r, a[0] + r*a[1], linewidth=1.2, color="orange", label="Geradenfit mit Parametern a=(" + str(a)+")")
plt.legend(loc='best', fancybox=True, framealpha=0.5)


plt.xlim(xmin=-10, xmax = 10)
plt.ylim(ymin=-10, ymax = 10)
plt.show()

plt.savefig('ols.png')
