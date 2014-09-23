``NotImplemented`` raised, should raise ``NotImplementedError``
===============================================================

Summary
-------

When a module wants to raise an exception indicating that some functionality is not implemented, the built-in exception type that it wants to use is ``NotImplementedError``, not ``NotImplemented``. Replace ``NotImplemented`` with ``NotImplementedError`` or else Python will raise a ``TypeError`` error at runtime and the module will not not successfully execute.

Description
-----------

``NotImplemented`` is a built-in constant used by some Python special methods (``__eq__``, ``__lt__``, etc.) to indicate that a specific type of comparison is not implemented within that special method.

Examples
----------

Description of error
....................

The author of the ``area`` function below has not finished implementing the function. To ensure that other programmers understand that the function is not yet available, the ``area`` function always returns ``NotImplemented`` whenever it is called. However, ``NotImplemented`` is not a valid object type for ``raise`` statements, so Python raises a ``TypeError`` whenever ``area`` is called.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):
        """TODO: implement me"""
        raise NotImplemented  # causes TypeError

    area(2, 4)

Solutions
---------

Replace ``NotImplemented`` with ``NotImplementedError``
.......................................................

The ``NotImplemented raised, should raise NotImplementedError`` is suppressed once the author of the function replaces ``NotImplemented`` with ``NotImplementedError``. 

.. code:: python

    def area(width, height):
        """TODO: implement me"""
        raise NotImplementedError  # ok now

    area(2, 4)

References
----------
- `Python Standard Library - Built-In Exceptions <https://docs.python.org/2/library/exceptions.html#exceptions.NotImplementedError>`_
- `Python Standard Library - Built-In Constants <https://docs.python.org/2/library/constants.html#NotImplemented>`_
