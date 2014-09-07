Do not assign a ``lambda`` expression, use a ``def``
====================================================

Summary
-------

Assigning a name to a ``lambda`` essentially duplicates the functionality of ``def``, in which case you should just use a ``def`` in order to avoid confusion and increase clarity.

Description
-----------

The sole advantage that a ``lambda`` expression has over a ``def`` is that the ``lambda`` can be anonymously embedded within a larger expression. If you are going to assign a name to a ``lambda``, you are better off just defining it as a ``def``.

Examples
----------

``lambda`` expression assigned to variable
...........................................

The following code assigns a ``lambda`` function which returns the double of its input to a variable. This is functionally identical to creating a ``def``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    f = lambda x: 2 * x

Solutions
---------

Use a ``def`` for named expressions
...................................

Refactor the ``lambda`` expression into a named ``def`` expression.

.. code:: python

    def f(x): return 2 * x
    
References
----------
- `Stack Overflow - Do not assign a lambda expression <http://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def>`_
