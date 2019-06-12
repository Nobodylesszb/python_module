#commonprefix()将路径列表作为参数，
# 并返回表示所有路径中存在的公共前缀的单个字符串。该值可能表示实际上不存在的路径，
# 并且路径分隔符未包含在考虑中，因此前缀可能不会在分隔符边界上停止。

import os.path
paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonprefix(paths))

"""
PATH: /one/two/three/four
PATH: /one/two/threefold
PATH: /one/two/three/

PREFIX: /one/two/three
"""