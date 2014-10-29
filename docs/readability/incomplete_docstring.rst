Incomplete docstring
====================

Summary
-------

A docstring for a module, function, class, or method is either missing or empty. Add a meaningful docstring comment to the object to improve code readability.

Description
-----------

Docstrings help you remember the intention of a module, function, class, or method. This is especially important as your codebase grows and it becomes harder to remember the implementation details of each object.

Examples
----------

Function missing docstring
..........................

The function below contains no docstring describing its purpose. If you didn't have access to the function implementation and only had access to the function signature (i.e. ``def area(width, height)``), you wouldn't be able to tell whether this function computes the area of a triangle or a rectangle.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):  # no docstring, bad
        return width * height

Solutions
---------

Add docstring to function
.........................

A short, concise docstring has been added to the modified example below to indicate that the function ``area`` computes the area of a rectangle.

.. code:: python

    def area(width, height):
        """ Returns the area of a rectangle. """
        return width * height

References
----------
- `Pylint - C0111 <http://pylint-messages.wikidot.com/messages:c0111>`_
- `PEP 257 - Docstring Conventions <http://legacy.python.org/dev/peps/pep-0257/>`_
