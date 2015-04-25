Bad first argument given to ``super()``
=======================================

``super()`` enables you to access the methods and members of a parent class without referring to the parent class by name. For a single inheritance situation the first argument to ``super()`` should be the name of the current child class calling ``super()``, and the second argument should be ``self`` (that is, a reference to the current object calling ``super()``).

Anti-pattern
------------

Python raises a ``TypeError`` when it attempts to execute the call to ``super()`` below. The first argument should be the name of the child class that is calling ``super()``. The author of the code mistakenly provided ``self`` as the first argument.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height

    class Square(Rectangle):
        def __init__(self, length):
            super(self, Square).__init__(length, length)  # bad first argument to super()

    s = Square(5)
    print s.area  # does not execute


Best practice
-------------

Insert name of child class as first argument to ``super()``
...........................................................

In the modified code below the author has fixed the call to ``super()`` so that the name of the child class which is calling ``super()`` (``Square`` in this case) is the first argument to the method.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height

    class Square(Rectangle):
        def __init__(self, length):
            super(Square, self).__init__(length, length)  # super() executes fine now

    s = Square(5)
    print s.area  # 25


References
----------

- `Python Standard Library - super([type[, object-or-type]]) <https://docs.python.org/3.1/library/functions.html#super>`_
- `Stack Overflow - What is a basic example of single inheritance using super()? <http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho>`_
- `Stack Overflow - Python super() inheritance and arguments needed <http://stackoverflow.com/questions/15896265/python-super-inheritance-and-arguments-needed>`_
- PyLint - E1003
