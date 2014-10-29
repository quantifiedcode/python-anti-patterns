Lambda may not be necessary
===========================

Summary
-------

The body of a lambda expression is just a function call on the same argument list as the lambda itself. This lambda is probably unnecessary. Improve code readability by removing the lambda and calling the function directly on the argument list.

Description
-----------

Lambda expressions enable you to create inline, anonymous functions. A lambda serves no purpose when it is just a call to a named function. It only makes the code harder to read. Remove the lambda and just call the function directly.

Examples
----------

Lambda is just a function call
..............................

The lambda expression below does nothing other than call the function ``multiply_by_two()``. In this situation the lambda is pointless and only makes the code harder to read.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def multiply_by_two(n):
        return n * 2

    anonymous_function = lambda x: multiply_by_two(x)  # unnecessary lambda

    anonymous_function(5)

Solutions
---------

Remove the lambda and call the function directly
................................................

The modified module below has removed the unnecessary lambda and just calls the ``multiply_by_two()`` function directly. This code is more direct and more concise than the original code that used a lambda.

.. code:: python

    def multiply_by_two(n):
        return n * 2

    multiply_by_two(5)
    
References
----------
- PyLint - W0108
- `Oliver Fromme <http://www.secnetix.de/olli/Python/lambda_functions.hawk>`_
