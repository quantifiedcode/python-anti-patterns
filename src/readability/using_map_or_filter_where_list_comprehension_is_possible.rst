Using ``map()`` or ``filter()`` where generator expression is possible
======================================================================

For simple transformations that can be expressed as a generator expression, use generator expressions over ``map()`` or ``filter()``. Use ``map()`` or ``filter()`` for expressions that are too long or complicated to express with a generator expression. Although a ``map()`` or ``filter()`` expression may be functionally equivalent to a generator expression, the generator expression is generally more concise and easier to read.

Anti-pattern
------------

The code below defines a list, and then uses ``map()`` to create a second iterable which is just the doubles of each value from the first list.

.. code:: python

    values = [1, 2, 3]
    doubles = map(lambda x: x * 2, values)

Best practice
-------------

Use generator expression instead of ``map()``
.............................................

In the modified code below, the code uses a generator expression to generate the second iterable yielding the doubled values from the first list. Although this is functionally equivalent to the first code, the generator expression is generally agreed to be more concise and easier to read.

.. code:: python

    values = [1, 2, 3]
    doubles = (x * 2 for x in values)
    
Use list comprehension instead of ``list(map())``
.................................................


.. code:: python

    values = [1, 2, 3]
    doubles = list(map(lambda x: x * 2, values))

In the modified code below, the code uses a list comprehension to generate the second list containing the doubled values from the first list. Although this is functionally equivalent to the first code, the generator expression is generally agreed to be more concise and easier to read.

.. code:: python

    values = [1, 2, 3]
    doubles = [x * 2 for x in values]

References
----------

- PyLint - W0110, deprecated-lambda
- `Oliver Fromme - list comprehensions <http://www.secnetix.de/olli/Python/list_comprehensions.hawk>`_
- `flake8-comprehensions <https://pypi.org/project/flake8-comprehensions/>`_
- `pyupgrade <https://github.com/asottile/pyupgrade>`_
