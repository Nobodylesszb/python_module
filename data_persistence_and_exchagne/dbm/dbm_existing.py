#要打开现有的数据库，使用flags的任何'r'（对于只读）或'w'（读-写）。
# 现有数据库会自动赋予whichdb()标识，因此只要可以识别文件，
# 就会使用相应的模块来打开它

import dbm

with dbm.open('/tmp/example.db', 'r') as db:
    print('keys():',db.keys())
    for k in db.keys():
        print('iterating:',k,db[k])
    print('db['author']=',db['author'])