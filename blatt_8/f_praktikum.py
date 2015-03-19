# coding: utf-8

# import matplotlib
# matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

y_data =np.array( [-0.032, 0.010, 0.057, 0.068, 0.076, 0.080, 0.031, 0.005, -0.041, -0.09, -0.088, -0.074])
x_data = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
x_data = x_data * np.pi/180

print("data")
print(x_data)
# ## baue design matrix
def f1(x):
    return np.cos(x)

def f2(x):
    return np.sin(x)
#
N = len(x_data)
X = np.zeros((N, 2))

X[:, 0] = f1(x_data)
X[:, 1] = f2(x_data)
print("X: ")
print(X)
print(np.dot(X.T, X))
M = np.dot( np.linalg.inv( np.dot(X.T, X) ) , X.T)
print("M: ")
print(M)

a = np.dot(M, y_data)
# a = [-0.0375, 0.0774]
print("a: ")
print(a)

plt.title("OLS")
plt.scatter(x_data, y_data, color="blue")
r = np.linspace(-10, 10, 100)
plt.plot(r, a[0]*f1(r) + f2(r)*a[1], linewidth=1.2, color="orange", label="Geradenfit mit Parametern a=(" + str(a)+")")
plt.legend(loc='best', fancybox=True, framealpha=0.5)

#
# plt.xlim(xmin=-0.1, xmax = 0.1)
# plt.ylim(ymin=-0.1, ymax = 0.1)
plt.show()

# plt.savefig('f_praktikum.png')
