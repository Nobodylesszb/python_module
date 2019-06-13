#内存中的方法有一些缺点，
# 使得它对于真实世界的用例来说是不切实际的，
# 主要是系统需要足够的内存来同时保存驻留在内存中的未压缩和压缩版本。
# 另一种方法是使用Compress和 Decompress对象以递增方式操作数据，
# 这样整个数据集就不必适合内存。

import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressed: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Flushed: {}'.format(binascii.hexlify(remaining)))

#此示例从纯文本文件中读取小块数据并将其传递给compress()。
# 压缩器维护压缩数据的内部缓冲区。由于压缩算法取决于校验和和最小块大小，因此压缩器可能无法在每次接收到更多输入时返回数据。如果它没有准备好整个压缩块，则返回一个空字节字符串。当所有数据都被输入时
# 该flush()方法强制压缩器关闭最终块并返回其余的压缩数据。

"""
output:
Compressed: b'7801'
buffering...
buffering...
buffering...
buffering...
buffering...
Flushed: b'55904b6ac4400c44f73e451da0f129b20c2110c85e696b8c40dde
dd167ce1f7915025a087daa9ef4be8c07e4f21c38962e834b800647435fd3b90
747b2810eb9c4bbcc13ac123bded6e4bef1c91ee40d3c6580e3ff52aad2e8cb2
eb6062dad74a89ca904cbb0f2545e0db4b1f2e01955b8c511cb2ac08967d228a
f1447c8ec72e40c4c714116e60cdef171bb6c0feaa255dff1c507c2c4439ec96
05b7e0ba9fc54bae39355cb89fd6ebe5841d673c7b7bc68a46f575a312eebd22
0d4b32441bdc1b36ebf0aedef3d57ea4b26dd986dd39af57dfb05d32279de'
"""