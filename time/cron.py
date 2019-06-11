""" 
@author: bo
@file: cron.py
@version:
@time: 2019/06/11
@function： 创建一个定时任务
"""

# import datetime
# from apscheduler.schedulers.background import BackgroundScheduler

# def job_func():
#     print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

# scheduler = BackgroundScheduler()
# # 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
# # scheduler .add_job(job_func, 'cron', month='1-3,7-9',day='0, tue', hour='0-3')
# scheduler .add_job(job_func, 'cron',minute='20-30')

# print('正在执行定时任务')
# scheduler.start()
# print('正在执行定时任务————————————————')

from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour=10,minute='37-40')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass