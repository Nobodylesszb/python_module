#重建对象的问题
# 使用自定义类时，被pickle的类必须出现在读取pickle的进程的命名空间中。
# 仅腌制实例的数据，而不是类定义。
# 类名用于查找构造函数以在unpickling时创建新对象。以下示例将类的实例写入文件。

import pickle
import sys


class SimpleObject:

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)


if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('preserve'))
    data.append(SimpleObject('last'))

    filename = sys.argv[1]

    with open(filename, 'wb') as out_s:
        for o in data:
            print('WRITING: {} ({})'.format(
                o.name, o.name_backwards))
            pickle.dump(o, out_s)

"""
output:
WRITING: pickle (elkcip)
WRITING: preserve (evreserp)
WRITING: last (tsal)
"""