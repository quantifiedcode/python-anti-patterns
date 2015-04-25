Assigning a `lambda` expression to a variable
=============================================

The sole advantage that a ``lambda`` expression has over a ``def`` is that the ``lambda`` can be anonymously embedded within a larger expression. If you are going to assign a name to a ``lambda``, you are better off just defining it as a ``def``.

From the PEP 8 Style Guide:

    Yes:

    def f(x): return 2*x

    No:

    f = lambda x: 2*x

    The first form means that the name of the resulting function object is specifically 'f' instead of the generic '<lambda>'. This is more useful for tracebacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression)

Anti-pattern
------------

The following code assigns a ``lambda`` function which returns the double of its input to a variable. This is functionally identical to creating a ``def``.

.. code:: python

    f = lambda x: 2 * x

Best practice
-------------

Use a ``def`` for named expressions
...................................

Refactor the ``lambda`` expression into a named ``def`` expression.

.. code:: python

    def f(x): return 2 * x

References
----------

- `PEP 8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_
- `Stack Overflow - Do not assign a lambda expression <http://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def>`_
- pep8 - E731
