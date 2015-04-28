Using an unpythonic loop
========================

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." Creating a loop that uses an incrementing index to access each element of a list within the loop construct is not the preferred style for accessing each element in a list. The preferred style is to use ``enumerate()`` to simultaneously retrieve the index and list element.

Anti-pattern
------------

The code below uses an index variable ``i`` in a ``for`` loop to iterate through the elements of a list. This is not the preferred style for iterating through a list in Python.

.. code:: python

    l = [1,2,3]

    for i in range(0,len(list)):  # creating index variable
        le = l[i]  # using index to access list
        print i,le

Best practice
-------------

Retrieve index and element when defining loop
.............................................

The updated code below demonstrates the Pythonic style for iterating through a list. When you define two variables in a ``for`` loop in conjunction with a call to ``enumerate()`` on a list, Python automatically assigns the first variable as an index variable, and the second variable as the corresponding list element value for that index location in the list.

.. code:: python

    for i, le in enumerate(l):
        print i, le

References
----------

- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
