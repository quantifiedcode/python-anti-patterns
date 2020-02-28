Using `type()` to compare types
===============================

The function ``isinstance`` is the best-equipped to handle type checking because it supports inheritance (e.g. an instance of a derived class is an instance of a base class, too). Therefore ``isinstance`` should be used whenever type comparison is required.

Anti-pattern
------------

The ``if`` statement below uses the pattern ``if type(OBJECT) is types.TYPE`` to compare a ``Rectangle`` object to a built-in type (``ListType`` in this example). This is not the preferred pattern for comparing types.

.. code:: python

    import types

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    # bad
    if type(r) is types.ListType:
        print("object r is a list")

Note that the following situation will raise the error, although it shouldn't.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Square(Rectangle):
        def __init__(self, length):
            super(Square, self).__init__(length, length)

    r = Rectangle(3, 4)
    s = Square(2)

    # bad
    if type(r) is not type(s):
        print("object types do not match")

Best practice
-------------

Use ``isinstance`` to compare types
...................................

The preferred pattern for comparing types is the built-in function ``isinstance``.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Square(Rectangle):
        def __init__(self, length):
            super(Square, self).__init__(length, length)

    r = Rectangle(3, 4)
    s = Square(2)

    # good
    if isinstance(s, Rectangle):
        print("object s is a Rectangle")

References
----------

- `Stack Overflow: Differences between isinstance() and type() in Python <http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python>`_



