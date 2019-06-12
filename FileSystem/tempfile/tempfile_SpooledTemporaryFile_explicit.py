import tempfile

with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)
    print('rolling over')
    temp.rollover()
    print(temp._rolled, temp._file)

"""
temp: <tempfile.SpooledTemporaryFile object at 0x0000023306424390>
False <_io.StringIO object at 0x0000023306432048>
False <_io.StringIO object at 0x0000023306432048>
False <_io.StringIO object at 0x0000023306432048>
rolling over
True <tempfile._TemporaryFileWrapper object at 0x0000023306424978>
"""