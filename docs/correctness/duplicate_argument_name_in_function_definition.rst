Duplicate argument name in function definition
==============================================

Summary
-------

Two arguments in a function definition have the same name. Rename the arguments to unique names, or else Python will raise a syntax error and the program will not execute.

Description
-----------

Having two or more arguments with the same name creates unresolvable ambiguity for the Python interpreter. Whenever the arguments with the same name are referenced in the function definition, Python cannot resolve exactly which argument is being referenced. As a result, Python returns a syntax error and the program cannot execute.

Examples
----------

Two arguments in function definition have same name
...................................................

The function ``multiply`` multiplies the two numbers passed as arguments and returns the product of the multiplication. Because both arguments are named ``n`` the Python interpreter cannot determine which argument is being referenced whenever the argument ``n`` is used in the function definition.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def multiply(n, n): # syntax error
        return n * n # Python cannot resolve which n is being referenced (arg 1 or arg 2?)
    
    multiply(3, 2) # 3 * 3, or 3 * 2, or 2 * 2?

Solutions
---------

Rename the arguments to unique names
....................................

The only solution for duplicate argument names is giving each argument a unique name. In the ``multiply`` function the two arguments have been given the unique names ``a`` and ``b``.

.. code:: python

    def multiply(a, b): # unique names
        return a * b # no more ambiguity
    
    multiply(3, 2) # returns 6
    
References
----------
