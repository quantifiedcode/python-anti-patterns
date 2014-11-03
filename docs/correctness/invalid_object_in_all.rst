Invalid object in ``__all__``
=============================

Summary
-------

The ``__all__`` list of a module contains an invalid object. The ``__all__`` list must only contain string literals that correspond to variables, functions, classes, and methods which have been implemented in the module and which you want to publically expose to other modules. If you perform a wildcard import of a module (i.e. ``from module import *``) on a module that includes a non-literal-string in its ``__all__`` list Python raises a ``NameError`` and the module does not execute.

Description
-----------

``__all__`` is a special list which enables a module to choose which variables, functions, classes, and methods it wants to publicly expose to other modules. ``__all__`` must only contain string literals. Each string literal must correspond to an object that has actually been implemented in the module. Note that this error is only triggered with wildcard imports (imports that follow the pattern ``from MODULE import *`` where ``MODULE`` is the name of the module containing the bad ``__all__`` list).

Examples
----------

``__all__`` list contains non-string-literal
............................................

The module below wants to expose its ``Rectangle`` class to other modules. ``__all__`` is supposed to contain string literals representing variables, classes, methods, and functions. But the module does not do this. It directly contains the name of the ``Rectangle`` class. Python raises the ``Invalid object in __all__`` error because of this.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """a.py"""

    __all__ = [Rectangle, "MESSAGE"]  # Rectangle causes NameError because it is not a string literal

    MESSAGE = "Hello, World!"

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

When the module below attempts to import ``a.py`` Python raises the ``Invalid object in __all__`` error because of the non-literal-string ``Rectangle`` that is defined in ``a.__all__``. If you were to attempt to execute this code Python would raise a ``NameError``. Note that this error is only triggered with wildcard imports (imports that follow the pattern ``from MODULE import *`` where ``MODULE`` is the name of the module containing the bad ``__all__`` list).

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    from a import *  # Causes NameError

    r = Rectangle(3, 6)  # does not execute


Solutions
---------

Only use string literals in ``__all__``
.......................................

The modified module below suppresses the ``Invalid object in __all__`` error by renaming ``Rectangle`` to ``"Rectangle"``.

.. code:: python

    """a.py"""

    __all__ = ["Rectangle:, "MESSAGE"]  # Changed Rectangle to "Rectangle"

    # ...
    
References
----------
- PyLint - E0604
