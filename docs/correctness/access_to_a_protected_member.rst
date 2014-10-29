Access to a protected member of a client class
==============================================

Summary
-------

A module has attempted to directly access a protected member (a member prefixed with ``_``) of a class. Either modify the member so that it is no longer protected, add the member to the module's ``__all__`` list, or use a public method to access the member.

Description
-----------

Treat this error as a warning. Although it violates the principles of object-oriented programming to directly access protected or private members, Python will have no problem executing the code.

Examples
----------

Problem: Module directly accesses protected member of class
...........................................................

The module below directly accesses the ``_width`` member of a Rectangle instance. ``_width`` is protected because it is prefixed with ``_``. This indicates that no code outside of the class is supposed to directly access the member.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self._width = width
            self._height = height

    r = Rectangle(5, 6)
    print "Width: {:d}".format(r._width)  # direct access of protected member

Solution: Use ``property`` to access the member
'''''''''''''''''''''''''''''''''''''''''''''''

For new-style classes (classes that derive from ``object``, e.g. ``class Rectangle(object):``) the Pythonic way to access members is to use the built-in Python function ``property()``.

.. code:: python

    class Rectangle(object):  # "new-style class" == 
                              # must derive from object to use property

        def __init__(self, width, height):
            self._width = width
            self._height = height

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._width = value
        
        @width.deleter
        def width(self):
            del self._width

    r = Rectangle(5, 6)
    print "Width: {:d}".format(r.width)  # automatically accesses getter, behind the scenes

Solution: Add protected member to ``__all__``
'''''''''''''''''''''''''''''''''''''''''''''

If the author of the class decides that it is accessible to directly access the protected member, he can add the protected member to the module's ``__all__`` class to indicate this. The code will execute either way, but this at least explicitly documents that it is acceptable to directly access the member.

.. code:: python

    __all__ = ["Rectangle", "_width"]  # protected member included in __all__

    class Rectangle(object):
        def __init__(self, width, height):
            self._width = width
            self._height = height

    r = Rectangle(5, 6)
    print "Width: {:d}".format(r._width)  # __all__ says this is OK

References
----------
- PyLint - W0212
- `Python Standard Library - property([fget[, fset[, fdel[, doc]]]]) <https://docs.python.org/2/library/functions.html#property>`_
