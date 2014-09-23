Unnecessary parens after keyword
================================

Summary
-------

This error is raised when parentheses are encountered after any of the following keywords: ``assert``, ``del``, ``elif``, ``except``, ``for``, ``if``, ``in``, ``not``, ``raise``, ``return``, ``while``, ``yield``, or ``print``. Python style conventions prefer that you remove the parentheses unless the parentheses are being used to clarify the expression's order of operations.

Description
-----------

Wrapping expressions in parentheses is a common style convention in C or Java, but it is not necessary in Python. Python style conventions prefer that you remove the parentheses when they are not needed. You should ignore this error if the expression performs a complicated computation and the parentheses help clarify the order of oprations.

Examples
----------

Unnecessary parentheses in ``return`` statement
...............................................

The ``area`` function below computes the area of a rectangle. The author of the function wrapped the statement ``width * height`` after the keyword ``return`` in parentheses. Python raises the ``Unnecessary parens after keyword`` because of the parentheses after the ``return`` keyword.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):
        return (width * height)  # unnecessary parentheses

Solutions
---------

Remove the parentheses
......................

The author of the module concluded that the parentheses in the return statement of the ``area`` function were unnecessary. To improve the readability of the code the author removed the parentheses.

.. code:: python

    def area(width, height):
        return width * height  # removed unnecessary parentheses
    
References
----------
- `PyLint - C0325 <http://pylint-messages.wikidot.com/messages:c0325>`_
