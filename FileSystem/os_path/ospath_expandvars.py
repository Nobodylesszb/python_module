#expandvars() 更通用，并扩展路径中存在的任何shell环境变量
import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print(os.path.expandvars('/path/to/$MYVAR'))

"""
output:
/path/to/VALUE
"""