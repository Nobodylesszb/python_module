#命名文件
# 在某些情况下，命名临时文件很重要。对于跨多个进程甚至主机的应用程序，
# 命名文件是在应用程序的各个部分之间传递它的最简单方法。该NamedTemporaryFile()
# 函数创建一个文件而不取消链接，因此它保留其名称（使用该name属性访问 ）。

import os
import pathlib
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

    f = pathlib.Path(temp.name)

print('Exists after close:', f.exists())

"""
temp:
  <tempfile._TemporaryFileWrapper object at 0x000002BA28D1D4A8>
temp.name:
  'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\tmpdzgy8oqz'
Exists after close: False
"""