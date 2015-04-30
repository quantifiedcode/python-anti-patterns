Method has no argument
======================

Unlike some programming languages, Python does not pass references to instance or class objects automatically behind the scenes. So the program must explicitly pass them as arguments whenever it wants to access any members of the instance or class within a method.

Anti-pattern
------------

In the ``Rectangle`` class below the ``area`` method attempts to return the value of the ``area`` instance variable. However, ``self.area`` is undefined because a reference to the instance object has not been explicitly passed as an argument to the method.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area(): # missing first argument "self"
            return self.area # self is undefined here

Class method is missing the ``cls`` keyword
...........................................

The method ``print_class_name`` attempts to print the name of the class. However, to programmatically access a class name, a method needs to have a reference to the class object. This is accomplished by passing the keyword ``cls`` as the first argument to the method. Because ``print_class_name`` does not do this, its reference to ``cls`` in the body of the method is undefined.

.. code:: python

    class Rectangle:
        @classmethod
        def print_class_name(): # missing first argument "cls"
            print("Hello, I am {0}!".format(cls)) # cls is undefined here


The method ``area`` computes the value of any rectangle. Currently this method is ambiguous. It is defined as a method of the ``Rectangle`` class, yet it does not reference any instance or class members. The method needs to explicitly state that it is a static method via the ``@staticmethod`` decorator.

.. code:: python

    class Rectangle:
        # "@staticmethod" should be here
        def area(width, height):
            return width * height

Best practices
--------------

Add the ``self`` parameter to instance methods
.................................................

To access the ``area`` member of a ``Rectangle`` instance the first argument of the ``area`` method needs to be a reference to the instance object, signified by the keyword ``self``.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area(self): # instance members now accessible because of "self"
            return self.area

Add the ``cls`` parameter to class methods
.............................................

To access the name of the class the ``print_class_name`` method needs to explicitly pass an argument to the class object. This is done by adding the keyword ``cls`` as the first argument of the method.

.. code:: python

    class Rectangle:
        @classmethod
        def print_class_name(cls): # class members now accessible, thanks to "cls"
            print("Hello, I am {0}!".format(cls))

Add the ``@staticmethod`` decorator to static methods
........................................................

If the method is a static method that does not need access to any instance members, then the method should be preceded by the ``@staticmethod`` decorator. This improves readability by helping clarify that the method should never rely on any instance members.

.. code:: python

    class Rectangle:
        # clarifies that the method does not need any instance members
        @staticmethod
        def area(width, height):
            return width * height

References
----------
- `PyLint - E0211 <http://pylint-messages.wikidot.com/messages:e0211>`_
