#The context manager returned by contextmanager() is derived from ContextDecorator, 
# so it also works as a function decorator.

import contextlib

@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        # Yield control, but not a value, because any value
        # yielded is not available when the context manager
        # is used as a decorator.
        yield 'abb'
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')


@make_context()
def normal():
    print('  inside with statement')\

@make_context()
def throw_error(err):
    raise err
    

print('Normal:')
normal()

print('\nHandled error:')
throw_error(RuntimeError('showing example of handling an error'))

print('\nUnhandled error:')
throw_error(ValueError('this exception is not handled'))

#As in the ContextDecorator example above, 
# when the context manager is used as a decorator the value yielded by the 
# generator is not available inside the function being decorated. 
# Arguments passed to the decorated function are still available, 
# as demonstrated by throw_error() in this example.

"""
output:
Normal:
  entering
  inside with statement
  exiting

Handled error:
  entering
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  exiting
Traceback (most recent call last):
  File "contextlib_contextmanager_decorator.py", line 43, in
<module>
    throw_error(ValueError('this exception is not handled'))
  File ".../lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "contextlib_contextmanager_decorator.py", line 33, in
throw_error
    raise err
ValueError: this exception is not handled
"""


