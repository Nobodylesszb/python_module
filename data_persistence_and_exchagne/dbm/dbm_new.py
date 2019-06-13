import dbm

with dbm.open('/tmp/example.db', 'n') as db:
    db['key'] = 'value'
    db['today'] = 'sunday'
    db['author'] = doug