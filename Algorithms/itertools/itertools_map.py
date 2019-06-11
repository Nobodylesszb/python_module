# 转换输入
# 内置map()函数返回一个迭代器，
# 它调用输入迭代器中值的函数，并返回结果。当任何输入迭代器耗尽时它会停止

def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


print('Doubles:')
for i in map(times_two, range(5)):
    print(i)

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print('\nStopping:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)

"""
Doubles:
0
2
4
6
8

Multiples:
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36

Stopping:
(0, 0, 0)
(1, 1, 1)
"""
#在第一个示例中，lambda函数将输入值乘以2.在第二个示例中，
# lambda函数将两个参数相乘，取自单独的迭代器，
# 并返回具有原始参数和计算值的元组。第三个示例在生成两个元组后停止，因为第二个范围已用尽。