Using `type()` to compare types
===============================

The function ``isinstance`` is the best-equipped to handle type checking because it supports inheritance (e.g. an instance of a derived class is an instance of a base class, too). Therefore ``isinstance`` should be used whenever type comparison is required.

Anti-pattern
------------

The ``if`` statement below uses the pattern ``if type(OBJECT) is typing.TYPE`` to compare a ``Rectangle`` object to a built-in type (``List`` in this example). This is not the preferred pattern for comparing types.

.. code:: python

    import typing

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    # bad
    if type(r) is typing.List:
        print("object r is a list")

Note that the following situation will not raise the error, although it should.

.. code:: python

    import typing

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Circle(object):
        def __init__(self, radius):
            self.radius = radius

    c = Circle(2)
    r = Rectangle(3, 4)

    # bad
    if type(r) is not type(c):
        print("object types do not match")

Best practice
-------------

Use ``isinstance`` to compare types
...................................

The preferred pattern for comparing types is the built-in function ``isinstance``.

.. code:: python

    import typing

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(3, 4)

    # good
    if isinstance(r, typing.List):
        print("object r is a list")

References
----------

- `Stack Overflow: Differences between isinstance() and type() in Python <http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python>`_
- `typing <https://docs.python.org/3/library/typing.html>`_ — Support for type hints (since Python 3.5)


