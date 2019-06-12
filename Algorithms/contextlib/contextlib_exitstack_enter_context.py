# Most context managers operate on one object at a time, such as a single file or database handle. 
# In these cases, the object is known in advance and the code using the context manager can be built around that one object. In other cases, 
# a program may need to create an unknown number of objects in a context, 
# while wanting all of them to be cleaned up when control flow exits the context. 
# ExitStack was created to handle these more dynamic cases.

# An ExitStack instance maintains a stack data structure of cleanup callbacks. 
# The callbacks are populated explicitly within the context, 
# and any registered callbacks are called in the reverse order when control flow exits the context.
# The result is like having multple nested with statements, except they are established dynamically.

#There are several ways to populate the ExitStack. 
# This example uses enter_context() to add a new context manager to the stack

import contextlib

@contextlib.contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield {}
    print('{} exiting'.format(i))


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


variable_stack(2, 'inside context')

"""
output:
0 entering
1 entering
inside context
1 exiting
0 exiting
"""