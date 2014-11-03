Undefined name in ``__all__``
=============================

Summary
-------

A variable name or function is included in ``__all__`` which does not exist in the module. This name should either be implemented in the module or removed from ``__all__`` because if someone attempts to use the undefined name Python will raise an ``ImportError`` and the program will not execute.

Description
-----------

The ``__all__`` keyword is a list which objects defined in a module are publically available for other modules to use. When a module includes a name in its ``__all__`` list that is not implemented anywhere in the module, Python raises a ``ImportError`` whenever another module attempts to use this undefined object.

Examples
----------

Object not implemented
......................

In the module ``colors`` below, the author forgot to implement the ``brown`` variable but included it in the modules ``__all__`` list. Including an entry in ``__all__`` that does not correspond to any object defined in the module raises the ``Undefined name in __all__`` error.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """colors.py"""
    # todo: implement "brown" variable
    blue = "blue"
    green = "green"
    __all__ = ["brown", "blue", "green"] # "brown" is undefined

Solutions
---------

Implement the object
....................

One way to suppress the ``undefined name in __all__`` error is to implement the missing object, like the updated module below.

.. code:: python

    """colors.py"""
    brown = "brown"  # brown is now implemented
    blue = "blue"
    green = "green"
    __all__ = ["brown", "blue", "green"]  # "brown" is ok now
    
Remove the object from the ``__all__`` list
...........................................

If the object is private (meaning it should not be listed in ``__all__``) or if the object is not implemented, then removing it from the ``__all__`` list also suppresses the ``Undefined name in __all__`` error.

.. code:: python

    """colors.py"""
    # todo: implement "brown" variable
    blue = "blue"
    green = "green"
    __all__ = ["blue", "green"]  # __all__ is ok now because "brown" has been removed

References
----------
- `Stack Overflow - Can someone explain __all__ in Python? <http://stackoverflow.com/questions/44834/can-someone-explain-all-in-python>`_
- Pyflakes - F822
