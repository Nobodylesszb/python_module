#for迭代多个序列的嵌套循环通常可以替换为product()，
# 这会产生单个可迭代，其值是输入值集的笛卡尔乘积。
from itertools import *
import pprint

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()

#由product()元组产生的值，从每个迭代中获取的成员按它们传递的顺序作为参数传入。
# 返回的第一个元组包含每个iterable的第一个值。首先处理传递给的最后一个迭代product()，
# 然后是倒数第二个，
# 依此类推。结果是返回值基于第一个可迭代，然后是下一个可迭代，等等
"""
 2H  2D  2C  2S 
 3H  3D  3C  3S 
 4H  4D  4C  4S 
 5H  5D  5C  5S 
 6H  6D  6C  6S 
 7H  7D  7C  7S 
 8H  8D  8C  8S 
 9H  9D  9C  9S 
10H 10D 10C 10S 
 JH  JD  JC  JS 
 QH  QD  QC  QS 
 KH  KD  KC  KS 
 AH  AD  AC  AS 
"""
