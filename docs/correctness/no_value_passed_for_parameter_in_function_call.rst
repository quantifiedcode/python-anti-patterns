No value passed for parameter in function call
==============================================

Summary
-------

One of the positional arguments required in a function call is empty. Provide a value for the argument or else Python will raise a ``TypeError`` at runtime and the program will not execute.

Description
-----------

When a positional argument is defined in a function definition, Python assumes that that data is required in order to successfully use the function. When a module calls a function and leaves one of these arguments empty, Python assumes that the function does not have all of the required data that it needs and therefore raises a ``TypeError`` and does not execute the program.

One way to suppress the error is to fix each function call to match the number of required arguments. Another way to fix the error is to specify default values for arguments that may not be supplied.

Examples
----------

Argument is empty in function call
..................................

The ``print_name`` function below prints the name supplied as arguments to standard output. It expects two arguments, ``first_name`` and ``last_name``. When the module below calls ``print_name`` it only provides an argument for ``first_name``. The ``last_name`` argument is left empty. When Python encounters this code it will raise a ``TypeError`` error at runtime and the program will not execute.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_name(first_name, last_name):
        print first_name, last_name

    print_name("John",)

Solutions
---------

Fix function call to match function definition
..............................................

Adding the missing second argument to the ``print_name`` function call suppresses the ``No value passed for parameter in function call`` error.

.. code:: python

    def print_name(first_name, last_name):
        print first_name, last_name

    print_name("John", "Smith")  # added value for missing parameter

Specify default value for argument
..................................

Specifying a default value for arguments is another way to suppress the ``No value passed for parameter in function call`` error. When the function is called and a value is not supplied for the argument, Python supplies the default value for whenever is used in the function definition.

.. code:: python

    def print_name(first_name, last_name = ""):  # added default value for last_name
        print first_name, last_name

    print_name("John", )  # OK now. Python subsitutes empty string for second argument

References
----------
