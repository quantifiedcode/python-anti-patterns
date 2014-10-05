Not using explicit unpacking
============================

Summary
-------

Rather than creating variables and then manually assigning a list item to each variable, use Python's built-in unpacking functionality to make your code less error-prone and more concise.

Description
-----------

When you see multiple variables being defined followed by an assignment to a list (e.g. ``l0, l1, l2 = l``, where ``l0``, ``l1``, and ``l2`` are variables and ``l`` is a list), Python will automatically iterate through the list and assign ``l[0]`` to ``l1``, ``l[1]`` to ``l1``, and so on.

Examples
----------

Not using unpacking
...................

The module below manually creates multiple variables to access the items in a list. This code is error-prone and unnecessarily verbose, as well as tedious to write.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    l = [4, 7, 18]

    l0 = l[0]
    l1 = l[1]
    l2 = l[2]

Solutions
---------

Use unpacking
.............

The modified module below is functionally equivalent to the original module, but this module is more concise and less prone to error.

.. code:: python

    l = [4, 7, 18]

    l0, l1, l2 = l
    
References
----------
