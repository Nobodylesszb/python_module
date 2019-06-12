#临时文件
# 需要临时文件来存储数据而不需要与其他程序共享该文件的应用程序应该使用该 
# TemporaryFile()函数来创建文件。该函数创建一个文件，并在可能的平台上立即取消链接。
# 这使得另一个程序无法找到或打开该文件，因为文件系统表中没有对它的引用。
# 创建的文件在TemporaryFile()关闭时会自动删除，
# 无论是通过调用close()还是使用上下文管理器API和with语句。

import os
import tempfile

print('Building a filename with PID:')
filename = '/FileSystem//tempfile/{}.txt'.format(os.getpid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

# Clean up the temporary file yourself.
os.remove(filename)

print()
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

"""
Building a filename with PID:
temp:
  <_io.BufferedRandom name='/tmp/guess_my_name.12151.txt'>
temp.name:
  '/tmp/guess_my_name.12151.txt'

TemporaryFile:
temp:
  <_io.BufferedRandom name=4>
temp.name:
  4
"""