import shelve

with shelve.open('test_shelf.db') as s:
    existing = s['key']

print(existing)


"""
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
"""