Passing unexpected keyword argument in function call
====================================================

Summary
-------

A keyword argument was passed to a function which does not accept keyword arguments. Either modify the function to accept keyword arguments, or remove the keyword arguments wherever the function is called, or else Python will raise a ``TypeError`` at runtime and the program will not execute.

Description
-----------

To be able to use keyword arguments in a function, the function definition must declar a formal argument in the form of ``**argument_name``. The double asterisk (``**``) indicates to Python that the function is going to use keyword arguments.

Examples
----------

Description of error
....................

The ``print_number`` function below prints out the number that has been supplied as an argument. Later on in the module the function is called with a keyword argument, ``number = 12``. The function definition does not expect keyword arguments, therefore Python raises a ``TypeError`` when the function is called with a keyword argument. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_number(n):
        print n

    print_number(n = 12)

Solutions
---------

Do not use keyword arguments with functions that do not support them
....................................................................

In the modified example below the module no longer attempts to pass a keyword argument to the ``print_number`` function, which eliminates the problem.

.. code:: python

    def print_number(n):
        print n

    print_number(12)

Modify the function to support keyword arguments
................................................

In the example below the modified version of the function ``print_number`` now supports keyword arguments. This suppresses the ``Passing unexpected keyword argument in function call`` error.

.. code:: python

    def print_number(**keyword_arguments):
        print keyword_arguments["n"]

    print_number(n = 12)

References
----------
- `Python Language Reference - Keyword Arguments <https://docs.python.org/2/tutorial/controlflow.html?highlight=keyword%20argument#keyword-arguments>`_
