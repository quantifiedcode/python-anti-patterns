Local variable name referenced before assignment
================================================

Summary
-------

In the definition of a function a variable name has been used before it has been assigned a value. The statement that assigns the variable a value must be placed before any statement that attempts to use the variable or else Python will raise a ``UnboundLocalError`` and the program will not execute.

Description
-----------

When a Python program attempts to use a variable that has not yet been assigned a value, Python effectively attempts to reference a value that does not exist in memory. Placing the statement that assigns a value to the variable before any other statement that attempts to use the variable effectively solves the error. It is a common practice in programming to place variable assignments at the very top of function definitions in order to avoid this error.

Examples
----------

Local variable used before it is assigned
.........................................

The ``area`` function below is supposed to return the area of a specified rectangle. The function attempts to print the value of the variable ``a`` before the variable has been assigned a value. When Python encounters this code it will raise a ``UnboundLocalError`` error and the program will not execute.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):
        print a # LocalBoundError: attempting to use variable before assignment
        a = width * height
        return a

Solutions
---------

Place variable assignment before variable use
.............................................

To suppress the ``Local variable name referenced before assignment`` error, place the statement that assigns the variable a value before any other statement which attempts to use the variable.

.. code:: python

    def area(width, height):
        a = width * height
        print a 
        return a
    
References
----------
