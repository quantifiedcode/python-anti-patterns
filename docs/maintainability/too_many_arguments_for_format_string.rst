Too many arguments for format string
====================================

Summary
-------

A format string contains more arguments than replacement fields. You can improve the readability and minimize the chance of bugs in the code by updating the format string to have the same number of replacement fields and arguments.

Description
-----------

Although a format string that contains more arguments than replacement fields will execute just fine, the extra arguments are unused. This reduces code readability and increases the chance of future bugs. Therefore, unless the extra arguments serve a purpose they should be removed. 

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

Now that the format string contains the same number of replacement fields (two) as arguments (two), the ``too many arguments for format string`` error is suppressed.

.. code:: python

    numbers = "{:d} {:d}".format(1, 2)  # removed the third argument
    print numbers
    
References
----------
