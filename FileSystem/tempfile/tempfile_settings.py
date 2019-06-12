# 临时文件位置
# 如果未使用dir参数给出显式目标，
# 则用于临时文件的路径将根据当前平台和设置而有所不同。
# 该tempfile模块包括两个用于查询运行时使用的设置的函数。

import tempfile

print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

"""
gettempdir(): C:\Users\ADMINI~1\AppData\Local\Temp
gettempprefix(): tmp
"""