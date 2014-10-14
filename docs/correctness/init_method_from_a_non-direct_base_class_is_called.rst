``__init__`` method from a non-direct base class is called
==========================================================

Summary
-------

A class has called the ``__init__`` method of another class which it is not a descendant of. Treat this as a warning and check to make sure that the class is not in fact supposed to descend from the other class.

Description
-----------

It is uncommon for a class to call the ``__init__()`` method of another class which it does not descend from. When you encounter this error, you should review the class in question and make sure that the current functionality is intended. If the class implementation is correct, consider leaving a comment for other programmers so that they too know to ignore this error in relation to this class.

Examples
----------

Class calls ``__init__()`` method of non-descendant class
.........................................................

In the module below, the ``Square`` class calls the ``__init__`` method of the ``Rectangle`` class, although in its current implementation ``Square`` does not descend from ``Rectangle``. This appears to be a mistake in the code implementation.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Square(object):  # if Square was a descendant this would be "class Square(Rectangle):"
        def __init__(self, length):
            Rectangle.__init__(self, width, height)  # calling __init__ of non-direct base class

    s = Square(5)



Solutions
---------

Modify the class to be a descendant of the other class
.......................................................

Upon reviewing the class implementations, the author decides that ``Square`` should be a descendant of ``Rectangle``. By replacing the statement ``class Square(object):`` with ``class Square(Rectangle):`` he makes ``Square`` a descendant of ``Rectangle``. This suppresses the ``__init__ method from a non-direct base class is called`` error.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

    class Square(Rectangle):  # Square is now a descendant of Rectangle
        def __init__(self, length):
            Rectangle.__init__(self, width, height)

    s = Square(5)

References
----------
- PyLint - W0233
