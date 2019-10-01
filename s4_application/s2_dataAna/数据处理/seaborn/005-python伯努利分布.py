# -*-coding:utf-8-*-

# from scipy.stats import bernoulli
#
# import seaborn as sb
#
# data_bern = bernoulli.rvs(size=1000, p=0.6)
#
# ax= sb.distplot(
#     data_bern,
#     kde= True,
#     color='crimson',
#     hist_kws={'linewidth':25,'alpha':1}
# )
#
# ax.set(xlabel='bernouli',ylabel='frequecy')




from scipy.stats import bernoulli
import seaborn as sb

data_bern = bernoulli.rvs(size=1000,p=0.6)
ax = sb.distplot(data_bern,
                  kde=True,
                  color='crimson',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Bernouli', ylabel='Frequency')
