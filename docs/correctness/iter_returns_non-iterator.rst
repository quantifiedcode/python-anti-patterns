``__iter__`` returns non-iterator
=================================

Summary
-------

Raised when the ``__iter__`` method of an iterable does not return a valid iterator. This error must be fixed when encountered, otherwise runtime errors will occur whenever a program attempts to use the container as an iterator.

Description
-----------

In order to properly implement Python's `iterator protocol <https://docs.python.org/2/library/stdtypes.html#iterator-types>`_ a container must implement an ``__iter__`` method that returns an iterator object. Python will raise the ``TypeError: __iter__ returned non-iterator of type %r`` whenever it attempts to iterate over a container that has not properly implemented the iterator protocol.

Examples
----------

``__iter__`` returns non-iterator
....................

In the ``Reverser`` class below the ``iter returns non-iterator`` error is raised because the ``__iter__`` method does not return an iterator such as ``self``. When Python attempts to execute the ``for`` loop a runtime error will occur because the ``__iter__`` method has not been properly implemented.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Reverser:
        """Iterable for reversing a string."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)
        def __iter__(self):
            return None  # Causes "iter returns non-iterator".
                         # Should return an iterator.
        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1 
            return self.data[self.index]

    r = Reverser("Hello, World!")
    for c in r:
        print c


Solutions
---------

Return a valid iterator in ``__iter__``
........................................

Modifying the ``__iter__`` method to return a valid iterator such as ``self`` suppresses the ``iter returns non-iterator`` error.

.. code:: python

    class Reverser:
        """Iterable for reversing a string."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)
        def __iter__(self):
            return self  # Now returns valid iterator.
        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1 
            return self.data[self.index]

    r = Reverser("Hello, World!")
    for c in r:
        print c

    
References
----------
- `The Python Tutorial - Iterators <https://docs.python.org/3/tutorial/classes.html#iterators>`_
- `The Python Language Reference - Iterator Types <https://docs.python.org/2/library/stdtypes.html#iterator-types>`_
- `Stack Overflow - Understanding Python's Iterator, Iterable, and Iteration Protocols <http://stackoverflow.com/questions/9884132/understanding-pythons-iterator-iterable-and-iteration-protocols-what-exact>`_
