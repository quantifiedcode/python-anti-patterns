Method has no argument
======================

Summary
-------

The first argument in an instance or class method must be a reference to the instance object (``self``) or class object (``cls``), respectively. Unlike some languages, Python does not pass these references automatically, so the program must explicitly pass them as arguments whenever it wants to access any members of the instance or class.

Examples
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
            return self.area # self is undefined here
            
Class method is missing the ``cls`` keyword
...........................................

In the ``Refrigerator`` class below the method ``print_class_name`` prints the name of the class. We know that ``print_class_name`` is a class method because of the function `decorator <https://docs.python.org/2/glossary.html#term-decorator>`_ ``@classmethod`` preceding it. ``print_class_name`` causes the ``Method has no argument`` error because it is missing the required first argument ``cls``.

.. code:: python

    class Refrigerator:
        @classmethod
        def print_class_name():
        print("Hello, I am %s!" % cls) # cls is undefined here

Solutions
-----------

Add the ``self`` parameter to the instance method
.................................................

To access the ``area`` member of the ``Rectangle`` instance the first argument of the ``area`` method needs to be a reference to the instance object, signified by the keyword ``self``.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area(self): # instance members now accessible, thanks to "self"
            return self.area
            
Add the ``cls`` parameter to the class method
.............................................

To access the name of the class the ``print_class_name`` method needs to explicitly pass an argument Adding the keyword ``cls`` as the first argument of ``print_class_name`` fixes the ``Method has no argument`` error.

.. code:: python

    class Refrigerator:
        @classmethod
        def print_class_name(cls): # class members now accessible, thanks to "cls"
            print("Hello, I am %s!" % cls)


References
----------
- `PyLint - E0211 <http://pylint-messages.wikidot.com/messages:e0211>`_
