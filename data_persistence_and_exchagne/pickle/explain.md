### pickle

#### explain
- The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes. This process is also called serializing the object. The byte stream representing the object can then be transmitted or stored, and later reconstructed to create a new object with the same characteristics.

- The documentation for pickle makes clear that it offers no security guarantees. In fact, unpickling data can execute arbitrary code. Be careful using pickle for inter-process communication or data storage, and do not trust data that cannot be verified as secure. See the hmac module for an example of a secure way to verify the source of a pickled data source.