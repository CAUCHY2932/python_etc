# -*-coding:utf-8-*-


from scipy import stats

rvs = stats.norm.rvs(loc=5,scale=10,size=(50,2))

print(stats.ttest_1samp(rvs))