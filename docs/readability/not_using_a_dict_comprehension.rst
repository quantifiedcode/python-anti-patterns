Not using a dict comprehension
==============================

Summary
-------

For Python versions 2.6 and below, a common way to initialize a dict is to pass an iterable of key-value pairs in the dict's constructor (e.g. ``d = dict((key, value) for (key, value) in iterable)``). However, in Python 2.7 and beyond, a new syntax called dict comprehension (e.g. ``d = {key: value for (key, value) in iterable}``) is available. Dict comprehension is generally more readable and is now the preferred style. Use dict comprehension whenever possible.

Description
-----------

You may encounter the old style of initializing a dict (passing an iterable of key-value pairs) in older Python code written before version 2.7. The new dict comprehension style is functionally equivalent and is much more readable. Consider refactoring the old-style code to use the new style (but only if you are using Python 2.7 or higher).

Examples
----------

Not using dict comprehension
............................

The module below demonstrates the old syntax of dict initialization. Although there is nothing syntactically wrong with this code, it is somewhat hard to read.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    l = [1,2,3]

    d = dict([(n,n*2) for n in l])  # hard to read

    print d  # {1: 2, 2: 4, 3: 6} 

Solutions
---------

Use dict comprehension
......................

The modified module below uses the new dict comprehension syntax which was introduced in Python 2.7. Although the modified code below is functionally equivalent to the original code above, this modified module is more readable.

.. code:: python

    l = [1, 2, 3]

    d = {n: n * 2 for n in l}

    print d  # {1: 2, 2: 4, 3: 6}
    
References
----------
- `Stack Overflow - Create a dictionary with list comprehesion <http://stackoverflow.com/questions/1747817/python-create-a-dictionary-with-list-comprehension>`_
