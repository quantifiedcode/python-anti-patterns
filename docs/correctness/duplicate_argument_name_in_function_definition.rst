Duplicate argument name in function definition
==============================================

Summary
-------

Two or more parameters in a function definition have the exact same name. Give each parameter a unique name or else Python will raise a ``SyntaxError`` at runtime and the program will not execute.

Description
-----------

When two or more parameters have the same name in a function definition, Python cannot resolve which parameter is being referenced. The only solution to this situation is to give each parameter a unique name. This is a good programming practice in general; names should not be overloaded with multiple meanings.

Examples
----------

Multiple parameters have same name in function definition
.........................................................

The ``print_string`` function below attempts to use two parameters, both of which are called ``string``. Because Python cannot figure out which parameter is being used whenever the name ``string`` is used in the function definition, it raises a ``SyntaxError`` and does not execute the function.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_string(string, string):
        print string  # parameter one or two? Python cannot resolve.
        print string

    print_string("A", "B")  # print out "A" or "B"? Python cannot resolve.

Solutions
---------

Make each parameter name unique
...............................

In the modified module below, the parameters have been given unique names to fix the ``Duplicate argument name in function definition`` error.

.. code:: python

    def print_string(string_one, string_two):
        print string_one
        print string_two

    print_string("A", "B")
    
References
----------
- Pyflakes - F831
