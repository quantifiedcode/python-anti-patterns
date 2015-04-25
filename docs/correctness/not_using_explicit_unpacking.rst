Not using explicit unpacking
============================

When you see multiple variables being defined followed by an assignment to a list (e.g. ``l0, l1, l2 = l``, where ``l0``, ``l1``, and ``l2`` are variables and ``l`` is a list), Python will automatically iterate through the list and assign ``l[0]`` to ``l0``, ``l[1]`` to ``l1``, and so on.

Anti-pattern
------------

The code below manually creates multiple variables to access the items in a list. This code is error-prone and unnecessarily verbose, as well as tedious to write.

.. code:: python

    l = [4, 7, 18]

    l0 = l[0]
    l1 = l[1]
    l2 = l[2]

Best practice
-------------

Use unpacking
.............

The modified code below is functionally equivalent to the original code, but this code is more concise and less prone to error.

.. code:: python

    l = [4, 7, 18]

    l0, l1, l2 = l
