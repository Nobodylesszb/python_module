from operator import *

a = -1
b = 5

print('a =', a)
print('b =', b)
print()

print('not_(a)     :', not_(a))
print('truth(a)    :', truth(a))
print('is_(a, b)   :', is_(a, b))
print('is_not(a, b):', is_not(a, b))

#not_()包括尾随下划线，因为它not 是一个Python关键字。 truth()应用在if语句中测试表达式或将表达式转换为a 时使用的相同逻辑bool。 i
# s_()实现is关键字使用的相同检查，并is_not()进行相同的测试并返回相反的答案。

"""
a = -1
b = 5

not_(a)     : False
truth(a)    : True
is_(a, b)   : False
is_not(a, b): True
"""