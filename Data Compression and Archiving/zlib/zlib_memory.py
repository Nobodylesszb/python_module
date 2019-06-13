#The simplest way to work with zlib requires holding all of the data to be compressed or decompressed in memory.

import zlib
import binascii

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed   :', len(compressed),
      binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)


#示例演示了少量数据的压缩版本可能比未压缩版本大。
# 虽然实际结果取决于输入数据，但观察小数据集的压缩开销很有意思
"""
output:
Original     : 26 b'This is the original text.'
Compressed   : 32 b'789c0bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a123d007f2f097e'
Decompressed : 26 b'This is the original text.'
"""