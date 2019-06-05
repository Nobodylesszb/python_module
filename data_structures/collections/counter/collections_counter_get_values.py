#访问计数
import collections
c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
#CounterKeyError对于未知物品不会加注。
# 如果输入中未显示某个值（如e本例所示），则其计数为0。
"""
output:
a : 3
b : 2
c : 1
d : 1
e : 0
"""