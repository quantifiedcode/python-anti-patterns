Using `type()` to compare types
===============================

The function ``isinstance`` is the best-equipped to handle type checking because it supports inheritance (e.g. an instance of a derived class is an instance of a base class, too). Therefore ``isinstance`` should be used whenever type comparison is required.

Anti-pattern
------------

The ``if`` statement below uses the pattern ``if type(OBJECT) is types.TYPE`` to compare a ``Rectangle`` object to a built-in type (``ListType`` in this example). This is not the preferred pattern for comparing types.

.. code:: python

    import types

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    if type(r) is types.ListType:  # bad
        print "object r is a list"

Note that the following situation will not raise the error, although it should.

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

    if type(r) is not type(c):  # bad
        print "object types do not match"

Best practice
-------------

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

    if isinstance(r, types.ListType):  # good
        print "object r is a list"

References
----------

- `Stack Overflow: Differences between isinstance() and type() in Python <http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python>`_
- pep8 - E721
