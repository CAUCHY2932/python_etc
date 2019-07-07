# -*-coding_:utf-8-*-

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(1, 1)

linestyles = [':', '--', '-.', '-']
deg_of_freedom = [1, 4, 7, 6]

for df, ls in zip(deg_of_freedom, linestyles):
    ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

plt.xlim(0, 10)
plt.ylim(0, 0.4)

plt.xlabel('value')
plt.ylabel('frequency')
plt.title('chi-square distribution')

plt.legend()
plt.show()
