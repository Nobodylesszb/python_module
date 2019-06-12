#最简单的使用方法shelve是通过DbfilenameShelf 课程。
# 它用于dbm存储数据。该类可以直接使用，也可以通过调用shelve.open()。

import shelve

with shelve.open('test_shelf.db') as s:
    s['key'] = {
        'int': 10,
        'float': 9.5,
        'string': 'Sample data',
    }
