#该array模块定义了一个非常类似于a的序列数据结构list，
# 除了所有成员必须具有相同的基本类型。
# 支持的类型都是数字或其他固定大小的基本类型，如字节

import array
import binascii

s = b'This is the array.'
a = array.array('b', s)
print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))

"""
As byte string: b'This is the array.'
As array      : array('b', [84, 104, 105, 115, 32, 105, 115, 32, 116, 104, 101, 32, 97, 114, 114, 97, 121, 46])
As hex        : b'54686973206973207468652061727261792e'
"""