# The try:except form can be replaced with contextlib.suppress() 
# to more explicitly suppress a class of exceptions happening anywhere 
# in the with block.

import contextlib

class NonFatalError(Exception):
    print('error occured')


def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of existing state'
    )


with contextlib.suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')

print('done')


"""
error occured
trying non-idempotent operation
done
"""