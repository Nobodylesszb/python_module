#获取上个月第一天和最后一天的日期
import datetime
import time

# today = datetime.date.today()
# print(today)
# mlast_day = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
# print(mlast_day)

# """
# output:
# 2019-06-11
# 2019-05-31
# """
# mfirst_day = datetime.date(mlast_day.year, mlast_day.month, 1)
# print(mfirst_day) # 2019-05-01

# #获得时间差

# start_time = datetime.datetime.now()
# time.sleep(5)
# end_time = datetime.datetime.now()
# print(start_time)
# print(end_time)

# """
# output:
# 2019-06-11 13:56:57.681902
# 2019-06-11 13:57:02.682107
# """
# d = (end_time - start_time).seconds
# print(d) # 5

# #计算当前时间向后8个小时的时间
# d1 = datetime.datetime.now()
# d2 = d1 + datetime.timedelta(hours = 8)
# print(d2) #2019-06-11 21:58:51.210277

# # 计算上周一和周日的日期
# today = datetime.date.today()
# today_weekday = today.isoweekday()
# print(today_weekday)
# last_sunday = today - datetime.timedelta(days=today_weekday)
# last_monday = last_sunday - datetime.timedelta(days=6)
# print(last_sunday)
# print(last_monday)
# """
# output:
# 2
# 2019-06-09
# 2019-06-03
# """


#计算指定日期当月最后一天的日期和本月天数
def eomonth(date_object):
    if date_object.month == 12:
        next_month_first_date = datetime.date(date_object.year+1,1,1)
    else:
        next_month_first_date = datetime.date(date_object.year, date_object.month+1, 1)
    return next_month_first_date - datetime.timedelta(1)

date = datetime.date(2017,12,20)

print(eomonth(date)) # 2017-12-31
print(eomonth(date).day) # 31