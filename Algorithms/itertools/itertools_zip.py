#内置函数zip()返回一个迭代器，它将几个迭代器的元素组合成元组
for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)

"""
(1, 'a')
(2, 'b')
(3, 'c')
"""