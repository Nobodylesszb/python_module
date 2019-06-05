#要删除现有元素并在单个操作中用新值替换它们，请使用heapreplace()
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heapq.heapify(data)
print('start:')
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))
    show_tree(data)


"""
output:
start:

                 4                  
        9                 12        
    10       11       19       15   
 17  20  22  27 
------------------------------------

replace  4 with  0:

                 0                  
        9                 12        
    10       11       19       15   
 17  20  22  27 
------------------------------------

replace  0 with 13:

                 9                  
        10                12        
    13       11       19       15   
 17  20  22  27 
------------------------------------
"""