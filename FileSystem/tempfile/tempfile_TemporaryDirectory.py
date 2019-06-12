#临时目录
# 当需要多个临时文件时，
# 使用TemporaryDirectory 并打开该目录中的所有文件创建单个临时目录可能更方便。
import pathlib
import tempfile

with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(the_dir)
    a_file = the_dir / 'a_file.txt'
    a_file.write_text('This file is deleted.')

print('Directory exists after?', the_dir.exists())
print('Contents after:', list(the_dir.glob('*')))

"""
C:\Users\ADMINI~1\AppData\Local\Temp\tmpt97ooa03
Directory exists after? False
Contents after: []
"""

