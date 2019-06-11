""" 
@author: bo
@file: interval.py
@version:
@time: 2019/06/111
@function： 创建一个间隔任务，每个2秒执行一次
"""

# import datetime
# import time
# from apscheduler.schedulers.background import BackgroundScheduler

# def timedTask():
#     print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

# if __name__ == '__main__':
#     # 创建后台执行的 schedulers
#     scheduler = BackgroundScheduler()  
#     # 添加调度任务
#     # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
#     scheduler.add_job(timedTask, 'interval', seconds=2)
#     # 启动调度任务
#     scheduler.start()
    
#     while True:
#         print(time.time())
#         time.sleep(5)
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


"""
output:
Tick! The time is: 2019-06-11 10:32:30.838007
Tick! The time is: 2019-06-11 10:32:33.839930
Tick! The time is: 2019-06-11 10:32:36.838303
Tick! The time is: 2019-06-11 10:32:39.838539
Tick! The time is: 2019-06-11 10:32:42.839151
Tick! The time is: 2019-06-11 10:32:45.838913
Tick! The time is: 2019-06-11 10:32:48.838586
Tick! The time is: 2019-06-11 10:32:51.837088
"""