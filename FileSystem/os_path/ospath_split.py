# Parsing Paths
# The first set of functions in os.path can be used to parse strings representing filenames into their component parts. It is important to realize that these functions do not depend on the paths actually existing; they operate solely on the strings.

# Path parsing depends on a few variable defined in os:

# os.sep - The separator between portions of the path (e.g., “/” or “\”).
# os.extsep - The separator between a filename and the file “extension” (e.g., “.”).
# os.pardir - The path component that means traverse the directory tree up one level (e.g., “..”).
# os.curdir - The path component that refers to the current directory (e.g., “.”).

#The split() function breaks the path into two separate parts and returns a tuple with the results. The second element of the tuple is the last component of the path, 
# and the first element is everything that comes before it.

import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

"""
output:
 '/one/two/three' : ('/one/two', 'three')
'/one/two/three/' : ('/one/two/three', '')
              '/' : ('/', '')
              '.' : ('', '.')
               '' : ('', '')
"""