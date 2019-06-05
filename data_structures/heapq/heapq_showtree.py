import math
from io import StringIO
def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()


"""
output:
random : [19, 9, 4, 10, 11]

add  19:

                 19                 
------------------------------------

add   9:

                 9                  
        19        
------------------------------------

add   4:

                 4                  
        19                9         
------------------------------------

add  10:

                 4                  
        10                9         
    19   
------------------------------------

add  11:

                 4                  
        10                9         
    19       11   
------------------------------------
"""