#除了压缩和解压缩功能外，
# zlib 还包括两个用于计算数据校验和的函数， 
# adler32()以及crc32()。校验和都不是加密安全的，
# 它们仅用于数据完整性验证。

import zlib

data = open('lorem.txt', 'rb').read()

cksum = zlib.adler32(data)
print('Adler32: {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.adler32(data, cksum)))

cksum = zlib.crc32(data)
print('CRC-32 : {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.crc32(data, cksum)))

"""
$ python3 zlib_checksums.py

Adler32:   3542251998
       :    669447099
CRC-32 :   3038370516
       :   2870078631
"""