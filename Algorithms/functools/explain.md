### functools

#### explain
- The functools module provides tools for adapting or extending functions and other callable objects, without completely rewriting them.
#### decorators
- The primary tool supplied by the functools module is the class partial, which can be used to “wrap” a callable object with default arguments. The resulting object is itself callable and can be treated as though it is the original function. It takes all of the same arguments as the original, and can be invoked with extra positional or named arguments as well. A partial can be used instead of a lambda to provide default arguments to a function, while leaving some arguments unspecified.