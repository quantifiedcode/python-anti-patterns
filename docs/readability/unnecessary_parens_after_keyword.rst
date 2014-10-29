Unnecessary parens after keyword
================================

Summary
-------

This error is raised when parentheses are encountered after any of the following keywords: ``assert``, ``del``, ``elif``, ``except``, ``for``, ``if``, ``in``, ``not``, ``raise``, ``return``, ``while``, ``yield``, or ``print``. Python style conventions prefer that you remove the parentheses unless the parentheses are being used to clarify the expression's order of operations.

Description
-----------

Wrapping expressions in parentheses is a common style convention in C or Java, but it is not necessary in Python. Python style conventions prefer that you remove the parentheses when they are not needed. You should ignore this error if the expression performs a complicated computation and the parentheses help clarify the order of operations.

Examples
----------

Unnecessary parentheses in ``return`` statement
...............................................

The ``area`` function below computes the area of a rectangle. The return value is wrapped in parentheses, which is unnecessary. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):
        return (width * height)  # unnecessary parentheses

Solutions
---------

Remove the parentheses
......................

The modified function below removes the unnecessary parentheses in the ``return`` statement.

.. code:: python

    def area(width, height):
        return width * height  # removed unnecessary parentheses
    
References
----------
- `PyLint - C0325 <http://pylint-messages.wikidot.com/messages:c0325>`_
