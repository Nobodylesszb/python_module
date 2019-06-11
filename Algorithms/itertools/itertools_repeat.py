#该repeat()函数返回一个迭代器，每次访问它时都会产生相同的值
from itertools import *

for i in repeat('over-and-over', 5):
    print(i)

"""
output:
over-and-over
over-and-over
over-and-over
over-and-over
over-and-over
"""