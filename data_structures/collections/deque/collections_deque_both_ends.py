# deques是线程安全的，因此甚至可以从单独的线程同时从两端消耗内容

import collections
import threading
import time

candle = collections.deque(range(5))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return

left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))


left.start()
right.start()

left.join()
right.join()

"""
output:
    Left: 0
   Right: 4
   Right: 3
    Left: 1
   Right: 2
    Left done
   Right done
"""