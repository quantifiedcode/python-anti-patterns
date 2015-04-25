Using a mutable default value as an argument
==============================================

Passing mutable lists or dictionaries as default arguments to a function can have unforeseen consequences. Usually when a programmer uses a list or dictionary as the default argument to a function, the programmer wants the program to create a new list or dictionary every time that the function is called. However, this is not what Python does. The first time that the function is called, Python creates a persistent object for the list or dictionary. Every subsequent time the function is called, Python uses that same persistent object that was created from the first call to the function.

Anti-pattern
------------

A programmer wrote the ``append`` function below under the assumption that the ``append`` function would return a new list every time that the function is called without the second argument. In reality this is not what happens. The first time that the function is called, Python creates a persistent list. Every subsequent call to ``append`` appends the value to that original list.

.. code:: python

    def append(number, list=[]):
        list.append(number)
        print list
        return list

    append(5) # expecting: [5], actual: [5]
    append(7) # expecting: [7], actual: [5, 7]
    append(2) # expecting: [2], actual: [5, 7, 2]


Best practice
-------------

Use a sentinel value to denote an empty list or dictionary
..........................................................

If, like the programmer who implemented the ``append`` function above, you want the function to return a new, empty list every time that the function is called, then you can use a `sentinel value <http://en.wikipedia.org/wiki/Sentinel_value>`_ to represent this use case, and then modify the body of the function to support this scenario. When the function receives the sentinel value, it knows that it is supposed to return a new list.

.. code:: python

    def append(number, list=None): # the keyword None is the sentinel value representing empty list
        if list is None:
            list = []
        list.append(number)
        print list
        return list

    append(5, None) # expecting: [5], actual: [5]
    append(7, None) # expecting: [7], actual: [7]
    append(2, None) # expecting: [2], actual: [2]

References
----------

- `PyLint - W0102 <http://pylint-messages.wikidot.com/messages:w0102>`_
- `Stack Overflow - Hidden Features of Python <http://stackoverflow.com/questions/101268/hidden-features-of-python#113198>`_
