#This first example Uses dumps() to encode a data structure as a string, 
# then prints the string to the console. 
# It uses a data structure made up of entirely built-in types. 
# Instances of any class can be pickled, 
# as will be illustrated in a later example.

import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('DATA:', end=' ')
pprint.pprint(data)

data_string = pickle.dumps(data)
print('PICKLE: {!r}'.format(data_string))

"""
DATA: [{'a': 'A', 'b': 2, 'c': 3.0}]
PICKLE: b'\x80\x03]q\x00}q\x01(X\x01\x00\x00\x00aq\x02X\x01\x00\x00\x00Aq\x03X\x01\
    x00\x00\x00bq\x04K\x02X\x01\x00\x00\x00cq\x05G@\x08\x00\x00\x00\x00\x00\x00ua.'
"""