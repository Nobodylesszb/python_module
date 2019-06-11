import datetime
# 获得当前时间
a = datetime.datetime.now() #2019-06-11 13:45:34.368954
print(a)

b = datetime.datetime.utcnow() #返回当前日期时间的UTC datetime对象
print(b) #2019-06-11 05:47:31.729653

#strptime(…)：根据string, format 2个参数，
# 返回一个对应的datetime对象
c = datetime.datetime.strptime('2017-3-22 15:25','%Y-%m-%d %H:%M')
print(c) # 2017-03-22 15:25:00