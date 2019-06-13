# update()可以重复调用哈希计算器的方法。
# 每次，摘要都会根据输入的附加文本进行更新。
# 逐步更新比将整个文件读入内存更有效，并产生相同的结果

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()


def chunkize(size, text):
    "Return parts of the text in size-based increments."
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return


h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('All at once :', all_at_once)
print('Line by line:', line_by_line)
print('Same        :', (all_at_once == line_by_line))

"""
All at once : e66ed2269e8a3aad3d8b06d944d0b8db
Line by line: e66ed2269e8a3aad3d8b06d944d0b8db
Same        : True
"""