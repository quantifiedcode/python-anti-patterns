Do not compare types, use ``isinstance()``
==========================================

Summary
-------

Raised when types are compared using the Python keyword ``is``. The preferred method for comparing types is the built-in function ``isinstance`` because it is specifically designed to robustly handle type comparisons on objects.

Description
-----------

The function ``isinstance`` is the best-equipped to handle type checking because it supports inheritance (e.g. an instance of a derived class is an instance of a base class, too). Therefore ``isinstance`` should be used whenever type comparison is required.

Examples
----------

Types compared using ``is``
.........................................

The ``if`` statement below uses the pattern ``if type(OBJECT) is types.TYPE`` to compare a ``Rectangle`` object to a built-in type (``ListType`` in this example). This is not the preferred pattern for comparing types.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import types

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    if type(r) is not types.ListType:
        print "object r is a list"
        
Note that the following situation will not raise the error.

.. code:: python

    import types

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Circle:
        def __init__(self, radius):
            self.radius = radius

    c = Circle(2)
    r = Rectangle(3, 4)

    if type(r) is not type(c):
        print "object types do not match"

Solutions
---------

Use ``isinstance`` to compare types
...................................

The preferred pattern for comparing types is the built-in function ``isinstance``.

.. code:: python

    import types

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    if isinstance(r, types.ListType):
        print "object r is a list"
        
References
----------
- `Stack Overflow: Differences between isinstance() and type() in Python <http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python>`_
