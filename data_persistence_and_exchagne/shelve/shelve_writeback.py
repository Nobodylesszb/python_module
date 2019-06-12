# 要自动捕获对存储在架子中的易失性对象的更改，
# 请在启用写回的情况下打开它。该writeback标志使货架记住使用内存缓存从数据库中检索的所有对象。
# 当货架关闭时，每个缓存对象也会写回数据库。
import shelve
import pprint
with shelve.open('test_shelf.db', writeback=True) as s:
    print('Initial data:')
    pprint.pprint(s['key'])

    s['key']['new_value'] = 'this was not here before'
    print('\nModified:')
    pprint.pprint(s['key'])

with shelve.open('test_shelf.db', writeback=True) as s:
    print('\nPreserved:')
    pprint.pprint(s['key'])


#虽然它减少了程序员错误的可能性，并且可以使对象持久性更加透明，
# 但在任何情况下都可能不希望使用回写模式。当磁盘架打开时，缓存会消耗额外的内存，
# 并且当它关闭时暂停将每个缓存的对象写回数据库会减慢应用程序的速度。所有缓存的对象都写回数据库，因为无法判断它们是否已被修改。
# 如果应用程序读取的数据多于写入数据，则回写将不必要地影响性能。

"""
output:
Initial data:
{'float': 9.5, 'int': 10, 'string': 'Sample data'}

Modified:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}

Preserved:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}

"""