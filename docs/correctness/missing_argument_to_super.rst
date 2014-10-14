Missing argument to ``super()``
===============================

Summary
-------

No arguments are provided to ``super()``. Python will raise the following error when ``super()`` is called with no arguments: ``TypeError: super() takes at least 1 argument``. The first argument to ``super()`` should be the class name of the child class that is calling the ``super()`` method of its parent. The second argument should be ``self``, which is a reference to the object calling its parent's ``super()`` method. Note that this error is only raised for Python versions 2.x which support new-style classes.

Description
-----------

``super()`` enables you to access the methods and members of a parent class without referring to the parent class by name. For a single inheritance situation the first argument to ``super()`` should be the name of the current child class calling ``super()``, and the second argument should be ``self``, that is, a reference to the current object calling ``super()``.

.. note::
    This error is only raised for Python versions 2.x which support new-style classes.

Examples
----------

No arguments given to ``super()``
.................................

The author of the module below provides no arguments for the child class' call to ``super()``. Python raises a ``TypeError`` at runtime because it expects at least 1 argument for ``super()``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height

    class Square(Rectangle):
        def __init__(self, length):
            super().__init__(length, length)  # no arguments provided to super()

    s = Square(5)
    print s.area  # does not execute


Solutions
---------

Insert name of child class as first argument to ``super()``
...........................................................

In the modified module below the author has fixed the call to ``super()`` so that the name of the child class which is calling ``super()`` (``Square`` in this case) is the first argument to the method, and a reference to the object calling ``super()`` is the second argument.

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
- PyLint - E1004
- `Python Standard Library - super([type[, object-or-type]]) <https://docs.python.org/3.1/library/functions.html#super>`_
- `Stack Overflow - What is a basic example of single inheritance using super()? <http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho>`_
- `Stack Overflow - Python super() inheritance and arguments needed <http://stackoverflow.com/questions/15896265/python-super-inheritance-and-arguments-needed>`_

