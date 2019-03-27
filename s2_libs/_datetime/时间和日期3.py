import datetime


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
            start_time = (now - datetime.timedelta(days=timedelta-1)).strftime("%Y-%m-%d")
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


if __name__ == '__main__':
    start, now = TimeHelper.acquire_start_and_end_time(time_level='day')
    # lst = TimeHelper.acquire_time_series(time_level='day')
    print(start, now)
    # print(lst)
