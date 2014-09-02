Method could be a function
==========================

Summary
-------

A static method is not preceded by the ``@staticmethod`` function decorator, or a class method is not preceded by the ``@classmethod`` function decorator.

Example(s)
----------

Static method is not preceded by ``@staticmethod`` decorator
...............................................

In the ``Rectangle`` class below the ``area`` method calculates the area of any rectangle given a width and a height.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height    
        def area(width, height):
            return width * height
            
``area`` causes the ``Method could be a function`` error because it is ambiguous. ``area`` could be a method belonging to the ``Rectangle`` class, or it could just be a global function that only *appears* to be nested inside of the ``Rectangle`` class (but is actually callable from anywhere in the program). In other words, the code above is actually equivalent to the code below.

.. code:: python
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height  
    def area(width, height):
        return width * height
            
Class method is not preceded by ``@classmethod`` decorator
...............................................

In the ``Rectangle`` class below the ``print_class_name`` method prints the name of the class.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height     
        def print_class_name:
            print "class name: Rectangle"
            
The code itself does not contain enough information to indicate that ``print_class_name`` is a class method. The code above is equivalent to the code below.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height     
    def print_class_name:
        print "class name: Rectangle"

Solution(s)
-----------

Add the ``@staticmethod`` decorator before the static method
............................................................

.. code:: python

    class Rectangle:
        @staticmethod
        def area(width, height):
            return width * height


Add the ``@classmethod`` decorator before the class method
..........................................................

.. code:: python

    class Rectangle:
        @classmethod
        def print_class_name:
            print "Rectangle"

Insert the ``cls`` keyword into the body of the static method
.............................................................

.. code:: python

    class Rectangle:
        def print_class_name:
            print("class name: %s" % cls) // "class name: Rectangle"

References
----------
- `PyLint - R0201 <http://pylint-messages.wikidot.com/messages:r0201>`_
