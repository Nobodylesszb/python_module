#要将相对路径转换为绝对文件名，请使用 abspath()

import os
import os.path

os.chdir('/FileSystem/os_path/')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))