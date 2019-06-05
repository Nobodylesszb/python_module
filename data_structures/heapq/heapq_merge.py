import heapq
import random

"""
将几个排序的序列组合成一个新序列对于小数据集来说很容易。

list(sorted(itertools.chain(*data)))
对于较大的数据集，此技术可以使用大量内存。
不是对整个组合序列进行排序，而是merge() 
使用堆一次生成一个项目的新序列，使用固定数量的内存确定下一个项目
"""


random.seed(2016)

data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for i, d in enumerate(data):
    print('{}: {}'.format(i, d))

print('\nMerged:')
for i in heapq.merge(*data):
    print(i, end=' ')
print()