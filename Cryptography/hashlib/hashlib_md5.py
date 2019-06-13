import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

"""
e66ed2269e8a3aad3d8b06d944d0b8db
"""