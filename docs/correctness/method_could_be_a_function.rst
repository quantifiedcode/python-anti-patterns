Method could be a function
==========================

When a method is not preceded by the ``@staticmethod`` or ``@classmethod`` decorators and does not contain any references to the class or instance (via keywords like ``cls`` or ``self``), Python raises the  ``Method could be a function`` error. This is not a critical error, but you should check the code in question in order to determine if this section of code really needs to be defined as a method of this class.

Anti-pattern
------------

In the ``Rectangle`` class below the ``area`` method calculates the area of any rectangle given a width and a height.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        # should be preceded by @staticmethod here
        def area(width, height): # causes "Method could be a function" error
            return width * height

``area`` causes the ``Method could be a function`` error because it is ambiguous. It does not reference the instance or class using the ``self`` or ``cls`` keywords and it is not preceded by the ``@staticmethod`` decorator.

Class method is not preceded by ``@classmethod`` decorator
..........................................................

In the ``Rectangle`` class below the ``print_class_name`` method prints the name of the class. Again, Python raises the ``Method could be a function`` error because the method does not reference any class members or methods and is not preceded by the ``@classmethod`` decorator.

Furthermore, the first argument of a class method must be a reference to the class itself.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        # should be preceded by @classmethod here
        def print_class_name: # missing required first argument "cls"
            print "class name: Rectangle"


Best practices
--------------

Add the ``@staticmethod`` decorator before the static method
............................................................

All static methods must be preceded by the ``@staticmethod`` decorator.

.. code:: python

    class Rectangle:
        @staticmethod # clarifies that this is a static method and belongs here
        def area(width, height):
            return width * height


Add the ``@classmethod`` decorator before the class method
..........................................................

All class methods must be preceded by the ``@classmethod`` decorator. Furthermore, the first argument of any class method must be ``cls``, which is a reference to the class itself.

.. code:: python

    class Rectangle:
        @classmethod
        def print_class_name(cls):
            print("class name: {0}".format(cls)) # "class name: Rectangle"

References
----------
- `PyLint - R0201 <http://pylint-messages.wikidot.com/messages:r0201>`_
