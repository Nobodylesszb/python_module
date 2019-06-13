import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest()) #7157b74bfbb662996d32d2dc7f65d9fc779d065f