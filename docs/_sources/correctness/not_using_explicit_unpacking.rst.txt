Not using explicit unpacking
============================

When you see multiple variables being defined followed by an assignment to a list (e.g. ``elem0, elem1, elem2 = elems``, where ``elem0``, ``elem1``, and ``elem2`` are variables and ``elems`` is a list), Python will automatically iterate through the list and assign ``elems[0]`` to ``elem0``, ``elems[1]`` to ``elem1``, and so on.

Anti-pattern
------------

The code below manually creates multiple variables to access the items in a list. This code is error-prone and unnecessarily verbose, as well as tedious to write.

.. code:: python

    elems = [4, 7, 18]

    elem0 = elems[0]
    elem1 = elems[1]
    elem2 = elems[2]

Best practice
-------------

Use unpacking
.............

The modified code below is functionally equivalent to the original code, but this code is more concise and less prone to error.

.. code:: python

    elems = [4, 7, 18]

    elem0, elem1, elem2 = elems


