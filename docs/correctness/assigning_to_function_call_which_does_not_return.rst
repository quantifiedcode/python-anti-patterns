Assigning to a function call which does not return
==================================================

Summary
-------

A name has been assigned to a function which does not contain a ``return`` statement. The only possible value for that name is ``None``, which could be potentially dangerous if a module expects some other value. Treat this error as a warning to go back and check the function to make sure that it is implemented correctly.

Description
-----------

A function that does not contain a ``return`` statement always returns ``None``. When a variable is assigned to a function like that, the only possible value for that variable is ``None``, which is not particularly useful and could be dangerous if that variable is used as input.

Examples
----------

Description of error
....................

The module below defines a function named ``hello`` which prints out the string ``Hello, World!`` and then assigns that function to a variable named ``h``. Because ``hello`` does not contain a return statement the only possible value of ``h`` is ``None``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def hello():
        print "Hello, World!"

    h = hello()  # only possible value is None

Solutions
---------

Modify the function to include a return statement
.................................................

Upon reviewing the module, the author realized that the ``hello`` function was not implemented correctly. It was supposed to return the string ``Hello, World!``, not print it out. The ``assigning to function call which does not return`` error is now suppressed.

.. code:: python

    def hello():
        return "Hello, World!"

    h = hello()  # OK now, value of "Hello, World!"

References
----------
- Pylint - E1111
