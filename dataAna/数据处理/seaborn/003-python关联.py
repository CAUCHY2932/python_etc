# -*-coding:utf-8-*-
# y
import matplotlib.pyplot as plt

import seaborn as sns

df= sns.load_dataset('iris')

#without regression

sns.pairplot(df, kind='scatter')
plt.show()