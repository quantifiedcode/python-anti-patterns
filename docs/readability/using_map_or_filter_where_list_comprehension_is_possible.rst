Using ``map()`` or ``filter()`` where list comprehension is possible
====================================================================

Summary
-------

Raised when a module defines a list, and then uses ``map()`` or ``filter()`` to perform a simple transformation on the original list. If the expression is simple enough that it can be expressed with a list comprehension, then the Python community prefers that you use list comprehensions. ``map()`` and ``filter()`` should be reserved for complicated transformations involving ``for`` or ``if`` statements.

Description
-----------

For simple transformations that can be expressed as a list comprehension, use list comprehensions over ``map()`` or ``filter()``. Use ``map()`` or ``filter()`` for expressions that are too long or complicated to express with a list comprehension. Although a ``map()`` or ``filter()`` expression may be functionally equivalent to a list comprehension, the list comprehension is generally more concise and easier to read.

Examples
----------

Using ``map()`` where list comprehension is possible
....................................................

The module below defines a list, and then uses ``map()`` to create a second list which is just the doubles of each value from the first list.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    values = [1, 2, 3]
    doubles = map(lambda x: x * 2, values)

Solutions
---------

Use list comprehension instead of ``map()``
...........................................

In the modified module below, the module uses a list comprehension to generate the second list containing the doubled values from the first list. Although this is functionally equivalent to the first module, the list comprehension is generally agreed to be more concise and easier to read.

.. code:: python

    values = [1, 2, 3]
    doubles = [x * 2 for x in values]
    
References
----------
- PyLint - W0110
`Oliver Fromme - List Comprehensions <http://www.secnetix.de/olli/Python/list_comprehensions.hawk>`_
