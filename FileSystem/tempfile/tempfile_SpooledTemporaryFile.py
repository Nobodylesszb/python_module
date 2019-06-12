# 假脱机文件
# 对于包含相对少量数据的临时文件，使用a可能更有效，
# SpooledTemporaryFile因为它使用io.BytesIO或 io.StringIO缓冲区将文件内容保存在内存中，
# 直到达到阈值大小。
# 当数据量超过阈值时，它被“翻转”并写入磁盘，然后缓冲区被替换为正常 TemporaryFile()。

import tempfile

with tempfile.SpooledTemporaryFile(max_size=100,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)

"""
temp: <tempfile.SpooledTemporaryFile object at 0x1007b2c88>
False <_io.StringIO object at 0x1007a3d38>
False <_io.StringIO object at 0x1007a3d38>
True <_io.TextIOWrapper name=4 mode='w+t' encoding='utf-8'>
"""