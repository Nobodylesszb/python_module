import heapq
from heapq_showtree import show_tree
data = [19, 9, 4, 10, 11]

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)

"""
output:
random    : [19, 9, 4, 10, 11]
heapified :

                 4                  
        9                 19        
    10       11   
------------------------------------
"""