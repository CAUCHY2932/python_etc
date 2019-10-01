#Python 实现得到现在时间12个月前的每个月
import datetime
# 假设现在的时间是2016年9月25日

#得到现在的时间  得到now等于2016年9月25日
now = datetime.datetime.now()
#得到今年的的时间 （年份） 得到的today_year等于2016年
today_year = now.year
#今年的时间减去1，得到去年的时间。last_year等于2015
last_year =  int(now.year) -1
#得到今年的每个月的时间。today_year_months等于1 2 3 4 5 6 7 8 9，
today_year_months = range(1,now.month+1)
#得到去年的每个月的时间  last_year_months 等于10 11 12 
last_year_months = range(now.month+1, 13)
#定义列表去年的数据
data_list_lasts = []
#通过for循环，得到去年的时间夹月份的列表
#先遍历去年每个月的列表
for last_year_month in last_year_months:
    # 定义date_list 去年加上去年的每个月
    date_list = '%s-%s' % (last_year, last_year_month)
    #通过函数append，得到去年的列表
    data_list_lasts.append(date_list)
    
data_list_todays = []
#通过for循环，得到今年的时间夹月份的列表
#先遍历今年每个月的列表
for today_year_month in today_year_months:
    # 定义date_list 去年加上今年的每个月
    data_list = '%s-%s' % (today_year, today_year_month)
    #通过函数append，得到今年的列表
    data_list_todays.append(data_list)
#去年的时间数据加上今年的时间数据得到年月时间列表
data_year_month = data_list_lasts + data_list_todays
data_year_month.reverse()