# -*- coding: utf-8 -*-
import datetime
import calendar
import time


def get_month_start_and_end():
    """获得月初和月末"""
    day_now = time.localtime()
    day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    _, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)
    day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)
    print('月初日期为：', day_begin, '月末日期为：', day_end)


def get_now_time():
    import time
    now = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    return now


def get_test():
    import calendar
    import time

    day_now = time.localtime()
    # 月初肯定是1号
    day_begin = '%d-%02d-01 00:00:00' % (day_now.tm_year, day_now.tm_mon)
    # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    _, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)
    day_end = '%d-%02d-%02d 24:00:00' % (day_now.tm_year,
                                         day_now.tm_mon, monthRange)
    print(day_begin, day_end)


def get_current_year():
    """获取当前年份
    返回形如 2019 的日期"""
    now = datetime.datetime.now()
    year = now.year
    return year


def get_current_time():
    """获取当前时间
    返回形如 2019-09-01 00:44:17.260009 的日期"""
    now = datetime.datetime.now()
    return now


def get_delta_date(d):
    """获取距离当前时间的时间差，以天为单位，如果求过去的时间，取负值
    返回形如 2019-08-29 00:52:49.319662 的日期，需要注意，当使用print打印这个值时，就会出现
    2019-08-29 00:52:49.319662
    >>> d = 5
    >>> get_delta_date(d)
    >>> datetime.datetime(2019, 8, 27, 0, 54, 59, 198563)
    """
    now = datetime.datetime.now()
    rv = now - datetime.timedelta(days=d)
    return rv


def funcname(self, parameter_list):
    pass


class TimeHelper:

    @classmethod
    def acquire_time_series(cls, time_level='day', time_range=12):
        """
        获取从当前时间起的，过去十二个周期（包含本周期）的日期字符串，
        并返回时间字符串组成的列表，默认为天，可选周
        :param time_level:
        :param time_range:
        :return:
        """
        now = datetime.datetime.now()
        if time_level == 'day':
            a = [(now - datetime.timedelta(days=x)).strftime("%Y-%m-%d")
                 for x in range(time_range)]
        elif time_level == 'month':
            this_year_months = ['{0}-{1:0>2}'.format(now.year, x)
                                for x in range(1, now.month+1)]
            last_year_months = ['{0}-{1:0>2}'.format(now.year-1, x)
                                for x in range(now.month+1, 13)]
            a = last_year_months + this_year_months
        else:
            a = []
        return a

    @classmethod
    def acquire_start_and_end_time(cls, time_level='day', timedelta=12):
        """
        获取当前时间和往前数第十一周期的日期，
        默认为天，可选周
        :param time_level:
        :param timedelta:
        :return:
        """
        now = datetime.datetime.now()
        if time_level == 'day':
            now_time = now.strftime('%Y-%m-%d')
            start_time = (now - datetime.timedelta(days=timedelta-1)
                          ).strftime("%Y-%m-%d")
        elif time_level == 'month':
            if now.month == 12:
                start_time = '{0}-{1:0>2}'.format(now.year, 1)
            else:
                start_time = '{0}-{1:0>2}'.format(now.year-1, now.month+1)
            now_time = '{0}-{1:0>2}'.format(now.year, now.month)
        else:
            now_time = ''
            start_time = ''
        return start_time, now_time


if __name__ == "__main__":
    # n = get_current_time()
    # n = get_current_year()
    n = get_delta_date(3)
    print(n)

    # start, now = TimeHelper.acquire_start_and_end_time(time_level='day')
    # # lst = TimeHelper.acquire_time_series(time_level='day')
    # print(start, now)
    # print(lst)
