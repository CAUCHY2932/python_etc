# -*-coding:utf-8-*-

import seaborn as sb

from matplotlib import pyplot as plt


df = sb.load_dataset('tips')

sb.regplot(x='total_bill', y='tip', data = df)

plt.show()

