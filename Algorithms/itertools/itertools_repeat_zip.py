#结合实用repeat()与zip()或map() 时不变值，需要包括与来自其他迭代器的值
from itertools import *

for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)

"""
output:
0 over-and-over
1 over-and-over
2 over-and-over
3 over-and-over
4 over-and-over
"""