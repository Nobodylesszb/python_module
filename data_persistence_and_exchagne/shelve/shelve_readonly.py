#该dbm模块不支持同时写入同一数据库的多个应用程序，但它支持并发只读客户端。
# 如果客户端不会修改架子，shelve请通过传递告诉 以只读方式打开数据库flag='r'
import dbm
import shelve

with shelve.open('test_shelf.db', flag='r') as s:
    print('Existing:', s['key'])
    try:
        s['key'] = 'new value'
    except dbm.error as err:
        print('ERROR: {}'.format(err))

"""
Existing: {'int': 10, 'float': 9.5, 'string': 'Sample data'}
"""