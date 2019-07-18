


import calendar
import time


def get_month_start_and_end():
    day_now = time.localtime()
    day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)
    print('月初日期为：',day_begin, '月末日期为：',day_end)


def get_now_time():
    import time
    now = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    return now

def get_test():
    import calendar
    import time

    day_now = time.localtime()
    day_begin = '%d-%02d-01 00:00:00' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    day_end = '%d-%02d-%02d 24:00:00' % (day_now.tm_year, day_now.tm_mon, monthRange)


    print(day_begin, day_end)

get_test()