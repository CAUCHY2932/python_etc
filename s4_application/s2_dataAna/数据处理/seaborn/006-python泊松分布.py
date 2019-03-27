# -*-coding:utf-8-*-

from scipy.stats import poisson
import seaborn as sb

data_binom=poisson.rvs(mu=4, size=10000)
ax=sb.distplot(
    data_binom,
    kde=True,
    color='green',
    hist_kws={'linewidth':25, 'alpha':1}
)

ax.set(xlabel='possion', ylabel='frequency')