Too many positional arguments for function call
===============================================

Summary
-------

A function has been called with more postional arguments than it accepts. Fix the function invocations to match the number of arguments defined in the function definition or else Python will raise a ``TypeError`` at runtime and the program will not execute.

Description
-----------

Positional arguments represent required pieces of data that a function needs in order to properly execute. Whenever a function is called, the function invocation must supply exactly as many arguments as is specified in the function definition. 

Examples
----------

Function called with too many arguments
.......................................

``print_name`` takes two arguments, one representing a first name and one a last name, and prints these arguments to standard output. In the module below someone attempts to pass three arguments to the function, one for a first name, one for a middle name, and one for a last name. This raises the ``Too many positional arguments for function call`` error and will raise a ``TypeError`` at runtime.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_name(first_name, last_name):
        print first_name, last_name

    print_name("Grace", "Patricia", "Kelly")

Solutions
---------

Update the function definition to support more arguments
........................................................

Updating the ``print_name`` function definition to support three arguments suppresses the ``Too many positional arguments for function call`` error.

.. code:: python

    def print_name(first_name, middle_name, last_name):
        print first_name, middle_name, last_name

    print_name("Grace", "Patricia", "Kelly")

Update the function invocation to match the function definition
...............................................................

Fixing the function invocation of ``print_name`` to match the number of arguments defined in the function defintion suppresses the error.

.. code:: python

    def print_name(first_name, last_name):
        print first_name, last_name

    print_name("Grace", "Kelly")

    
References
----------
- PyLint - E1121
