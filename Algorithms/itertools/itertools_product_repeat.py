from itertools import *

#要计算序列与自身的乘积，请指定输入应重复的次数
def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()


print('Repeat 2:\n')
print(list(product(range(3), repeat=2)))
show(list(product(range(3), repeat=2)))

print('Repeat 3:\n')
show(list(product(range(3), repeat=3)))

"""
Repeat 2:

[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
(0, 0) (0, 1) (0, 2) 
(1, 0) (1, 1) (1, 2) 
(2, 0) (2, 1) (2, 2) 

Repeat 3:

(0, 0, 0) (0, 0, 1) (0, 0, 2) 
(0, 1, 0) (0, 1, 1) (0, 1, 2) 
(0, 2, 0) (0, 2, 1) (0, 2, 2) 
(1, 0, 0) (1, 0, 1) (1, 0, 2) 
(1, 1, 0) (1, 1, 1) (1, 1, 2) 
(1, 2, 0) (1, 2, 1) (1, 2, 2) 
(2, 0, 0) (2, 0, 1) (2, 0, 2) 
(2, 1, 0) (2, 1, 1) (2, 1, 2) 
(2, 2, 0) (2, 2, 1) (2, 2, 2) 
"""