import collections
print('From the right:')
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print()

print('\nFrom the left:')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft(), end='\n')
    except IndexError:
        break
print()

"""
output:
From the right:
gfedcba

From the left:
0
1
2
3
4
5
"""