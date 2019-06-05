import heapq
from heapq_showtree import show_tree
data = [19, 9, 4, 10, 11]

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)