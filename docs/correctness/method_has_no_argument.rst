Method has no argument
======================

Summary
-------

The first argument in an instance method must be the keyword ``self``. The first argument in a class method must be the keyword ``cls``.

Example(s)
----------

Instance method is missing the ``self`` keyword
...............................................

In the ``Rectangle`` class below the ``area`` method returns the area of the instance. ``area`` causes the ``Method has no argument`` error because it is missing the required first argument ``self``.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area():
            return self.area
            
Class method is missing the ``cls`` keyword
...........................................

In the ``Refrigerator`` class below the method ``print_class_name`` prints the name of the class. We know that ``print_class_name`` is a class method because of the function `decorator <https://docs.python.org/2/glossary.html#term-decorator>`_ ``@classmethod`` preceding it. ``print_class_name`` causes the ``Method has no argument`` error because it is missing the required first argument ``cls``.

.. code:: python

    class Refrigerator:
        @classmethod
        def print_class_name():
        print("Hello, I am %s!" % cls)

Solution(s)
-----------

Add the ``self`` parameter to the instance method
.................................................

Adding the keyword ``self`` as the first argument of the ``area()`` method fixes the ``Method has no argument`` error.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area(self):
            return self.area
            
Add the ``cls`` parameter to the class method
.............................................

Adding the keyword ``cls`` as the first argument of ``print_class_name`` fixes the ``Method has no argument`` error.

.. code:: python

    class Refrigerator:
        @classmethod
        def print_class_name(cls):
            print("Hello, I am %s!" % cls)


References
----------
- `PyLint - E0211 <http://pylint-messages.wikidot.com/messages:e0211>`_
