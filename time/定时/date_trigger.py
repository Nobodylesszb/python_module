""" 
@author: bo
@file: date_trigger.py
@version:
@time: 2019/06/111
@function： 创建一个指定时间更新的任务
"""

from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler

def job_func(text):
    print(text)

scheduler = BackgroundScheduler()
# 在 2019-6-11 时刻运行一次 job_func 方法
scheduler .add_job(job_func, 'date', run_date=date(2019, 6, 11), args=['text'])
# 在 2019-6-11 14:00:00 时刻运行一次 job_func 方法
scheduler .add_job(job_func, 'date', run_date=datetime(2019, 6, 11, 14, 0, 0), args=['text'])
# 在 2019-6-1 14:00:01 时刻运行一次 job_func 方法
scheduler .add_job(job_func, 'date', run_date='2017-12-13 14:00:01', args=['text'])
print('任务正在执行')
scheduler.start()
