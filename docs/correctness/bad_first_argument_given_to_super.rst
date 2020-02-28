Bad first argument given to ``super()``
=======================================

``super()`` enables you to access the methods and members of a parent class without referring to the parent class by name. For a single inheritance situation the first argument to ``super()`` should be the name of the current child class calling ``super()``, and the second argument should be ``self`` (that is, a reference to the current object calling ``super()``).

.. note:: This anti-pattern only applies to Python versions 2.x, see "Super in Python 3" at the bottom of the page for the correct way of calling ``super()`` in Python 3.x.

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
            # bad first argument to super()
            super(self, Square).__init__(length)

    s = Square(5)
    print(s.area)  # does not execute


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
            # super() executes fine now
            super(Square, self).__init__(length)

    s = Square(5)
    print(s.area)  # 25


Super in Python 3
-----------------

Python 3 adds a new simpler ``super()``, which requires no arguments.  The correct way to call ``super()`` in Python 3 code is as follows.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height

    class Square(Rectangle):
        def __init__(self, length):
            # This is equivalent to super(Square, self).__init__(length)
            super().__init__(length)

    s = Square(5)
    print(s.area)  # 25

There are use cases where it is desirable to explicitly pass the subclass argument to ``super()`` e.g. a different class implements the function that is needed. However in most cases the parameterless call to ``super()`` is recommended, and needing to make frequent changes to the instance hierarchy may indicate a wider design issue.

Best practice
-------------

 * Use the parameterless call to ``super()`` as far as possible.
 * Refactor classes if it is becoming necessary to specify the sublass argument regularly.
  
References
----------

- `Python Standard Library - super([type[, object-or-type]]) <https://docs.python.org/3.1/library/functions.html#super>`_
- `Stack Overflow - What is a basic example of single inheritance using super()? <http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho>`_
- `Stack Overflow - Python super() inheritance and arguments needed <http://stackoverflow.com/questions/15896265/python-super-inheritance-and-arguments-needed>`_
- PyLint - E1003, bad-super-call
- `PEP 3135 - New Super <https://www.python.org/dev/peps/pep-3135/>`_
- `Real Python - A super() Deep Dive <https://realpython.com/python-super/#a-super-deep-dive>`_

