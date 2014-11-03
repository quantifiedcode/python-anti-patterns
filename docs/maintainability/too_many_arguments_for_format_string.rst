Too many arguments for format string
====================================

Summary
-------

A format string contains more arguments than replacement fields. Fix the format string so that it has the same number of replacement fields as argument strings to minimize bugs and improve readability.

Description
-----------

Although a format string that contains more arguments than replacement fields will execute, the extra arguments reduce code readability and increase the chance of future bugs. Therefore, unless the extra arguments serve a purpose they should be removed. 

Examples
----------

``print`` statement contains more arguments than replacement fields
...................................................................

The ``numbers`` variable in the module below uses ``format`` to programmatically insert arguments into replacement fields of a string literal. The ``too many arguments for format string`` error is raised on ``numbers`` because the format function contains three arguments, whereas the string only lists two replacement fields.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    numbers = "{:d} {:d}".format(1, 2, 3)
    print numbers

Solutions
---------

Remove extra arguments 
......................

The modified module below suppresses the ``too many arguments for format string`` error by fixing the format string to have the same number of replacement fields as arguments.

.. code:: python

    numbers = "{:d} {:d}".format(1, 2)  # removed the extra, third argument
    print numbers
    
Add more replacement fields
...........................

The modified module below adds another replacement field to the string literal to match the number of arguments passed to ``format()``. This is another way to fix the format string to have the same number of replacement fields as arguments.

.. code:: python

    numbers = "{:d} {:d} {:d}".format(1, 2, 3)  # added a third replacement field
    print numbers

References
----------
- PyLint - E1305
