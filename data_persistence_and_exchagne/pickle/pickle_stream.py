#除了dumps()和之外loads()，pickle还提供了处理类文件流的便利功能。
# 可以将多个对象写入流，
# 然后从流中读取它们，而无需事先知道写入了多少对象，或者它们有多大。

import io
import pickle
import pprint


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# Simulate a file.
out_s = io.BytesIO()

# Write to the stream
for o in data:
    print('WRITING : {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = io.BytesIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ    : {} ({})'.format(
            o.name, o.name_backwards))

#该示例使用两个BytesIO缓冲区模拟流。第一个接收pickle对象，它的值被送到第二个load()读取的对象。
# 简单的数据库格式也可以使用pickle来存储对象。该shelve模块就是这样一种实现

"""
output:
WRITING : pickle (elkcip)
WRITING : preserve (evreserp)
WRITING : last (tsal)
READ    : pickle (elkcip)
READ    : preserve (evreserp)
READ    : last (tsal)
"""