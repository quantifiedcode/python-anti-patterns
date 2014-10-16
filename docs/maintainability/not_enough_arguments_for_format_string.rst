Not enough arguments for format string
======================================

Summary
-------

A format string contains more replacement fields than arguments. When this occurs Python raises an ``IndexError`` at runtime and the module will not be able to successfully complete. Either remove the extra replacement fields or add more arguments.

Description
-----------

When Python encounters a format string, it programmatically replaces each replacement field with its corresponding argument provided in ``format()`` (i.e. the first replacement field is replaced with the first argument in ``format()``, the second replacement field is replaced with the second argument in ``format()``, etc.). Python does not check that the number of replacement fields is the same as the number of ``format()`` arguments. 

Examples
----------

Format string contains more replacement fields than arguments
.............................................................

The ``numbers`` variable in the module below uses ``format`` to programmatically insert arguments into replacement fields of a string literal. The ``not enough arguments for format string`` error is raised on ``numbers`` because the format function contains two replacement fields, whereas ``format()`` is only passed one argument.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    numbers = "{:d} {:d}".format(1)  # not enough args
    print numbers

Solutions
---------

Remove extra replacement fields
...............................

The modified module below removes the second replacement field. 

.. code:: python

    numbers = "{:d}".format(1)  # ok now, same number of fields as args
    print numbers
    
Add more arguments
..................

The modified module below adds a second argument to ``format()``. 

.. code:: python

    numbers = "{:d} {:d}".format(1, 2)  # ok now, same number of fields as args
    print numbers

References
----------
- PyLint - E1306
