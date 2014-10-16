Unused import
=============

Summary
-------

An imported module is not being used. Review the module in question for any missing implementations. If the module is not needed, remove the import statement to improve the readability of the code.

Description
-----------

Usually, when the ``unused import`` error is encountered, it means that someone began implementing a module but did not finish it. Other times, someone has refactored the module to no longer need a particular module, but that person forgot to remove the import statement. Therefore you should treat the ``unused import`` error as a warning and review the module in question.

Examples
----------

Imported module not used
........................

The module below imports the ``math`` module from the Python Standard Library but does not use any objects from the ``math`` module.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import math  # unused module, causes "unused import" error

    print "Hello, World!"

Solutions
---------

Remove the import statement
...........................

Upon reviewing the module, the author decides that the ``math`` module is not needed, so he removes the ``import math`` statement.

.. code:: python

    # removed import statement from here

    print "Hello, World!"

Finish implementing the module
..............................

Upon reviewing the module, the author realized that he forgot to implement a portion of the module. The ``import math`` statement served as a reminder that the module was not finished. Now that the module uses the ``factorial()`` function from the ``math`` module the ``unused import`` error is no longer raised.

.. code:: python

    import math

    print "Hello, World!"

    print "5! equals {:d}".format(math.factorial(5))  # math module used here, so no more error

References
----------
- PyLint - W0611
