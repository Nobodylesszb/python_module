#除了使用路径之外，
# os.path还包括用于检索文件属性的函数，类似于返回的函数 os.stat()：
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

"""
File         : d:\myownproject\python_module\FileSystem\os_path\ospath_properties.py
Access time  : Wed Jun 12 18:28:38 2019
Modified time: Wed Jun 12 18:30:00 2019
Change time  : Wed Jun 12 18:28:38 2019
Size         : 446
"""