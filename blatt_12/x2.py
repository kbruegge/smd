# coding: utf-8


import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from scipy.stats import norm

x = np.array([31.6, 32.2, 31.2, 31.9, 31.3, 30.8, 31.3])
mu = 30.7
sigma = 0.5

test = 1/(sigma**2) * np.sum( (x - mu)**2 )
# plt.plot(range,  norm.pdf(range, 0, 1), label="Standardnormalverteilung", color='orange', linewidth=1.7)

print(test)
