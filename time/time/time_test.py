import datetime
import time
import calendar
# 获取此时的时间
print (time.localtime())
"""
output
time.struct_time(tm_year=2019, tm_mon=6, tm_mday=11, tm_hour=11, tm_min=44, tm_sec=42, tm_wday=1, tm_yday=162, tm_isdst=0)
"""
#time.time()：返回当前时间的时间戳
print(time.time())  # 1560224901.8666422

#time.mktime(t)：将一个struct_time转化为时间戳
print(time.mktime(time.localtime())) # 1560224989.0

#time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入
print(time.asctime()) # Tue Jun 11 11:51:34 2019

#time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。
# 如果参数未给或者为None的时候，将会默认time.time()即当前时间戳为参数。
# 它的作用相当于time.asctime(time.localtime(secs))

print(time.ctime()) #Tue Jun 11 11:54:52 2019

#time.strftime(format[,t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
# 如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。

print(time.strftime(r"%Y-%m-%d %x")) #2019-06-11 06/11/19



