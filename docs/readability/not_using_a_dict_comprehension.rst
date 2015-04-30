Not using dict comprehensions
=============================

You may encounter the old style of initializing a dict (passing an iterable of key-value pairs) in older Python code written before version 2.7. The new dict comprehension style is functionally equivalent and is much more readable. Consider refactoring the old-style code to use the new style (but only if you are using Python 2.7 or higher).

Anti-pattern
------------

The code below demonstrates the old syntax of dict initialization. Although there is nothing syntactically wrong with this code, it is somewhat hard to read.

.. code:: python

    numbers = [1,2,3]

    my_dict = dict([(number,number*2) for number in numbers])  # hard to read

    print my_dict  # {1: 2, 2: 4, 3: 6}

Best practice
-------------

The modified code below uses the new dict comprehension syntax which was introduced in Python 2.7.

.. code:: python

    numbers = [1, 2, 3]

    my_dict = {number: number * 2 for number in numbers}

    print my_dict # {1: 2, 2: 4, 3: 6}

References
----------

- `Stack Overflow - Create a dictionary with list comprehesion <http://stackoverflow.com/questions/1747817/python-create-a-dictionary-with-list-comprehension>`_
