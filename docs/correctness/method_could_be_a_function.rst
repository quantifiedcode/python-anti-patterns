Method could be a function
==========================

Summary
-------

Python has encountered an ambiguous section of code that could either be a static method, class method, or global function.

Description
-----------

When a method is not preceded by the ``@staticmethod`` or ``@classmethod`` decorators and does not contain any references to the class (via keywords like ``cls``), Python raises ``Method could be a function`` error because it cannot determine the exact nature of the code. In this scenario the could even be a global function that is not even related to the class; it only appears to be because it is indented like a member of the class.

Examples
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
            
``area`` causes the ``Method could be a function`` error because it is ambiguous. ``area`` could be a method belonging to the ``Rectangle`` class, or it could just be a global function that only *appears* to be nested inside of the ``Rectangle`` class (but is actually callable from anywhere in the program). The code above is actually equivalent to the code below.

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

In the ``Rectangle`` class below the ``print_class_name`` method prints the name of the class. Again, Python cannot determine whether this a class method or just a global function that only appears to be a class member because of the way it is indented.

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

Solutions
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

The problem with the previous version of ``print_class_name`` is that it is ambiguous. Python cannot determine if it is associated to the class, or if it is actually a global function. When possible, adding the keyword ``cls`` to the function will remove the ambiguity. 

.. code:: python

    class Rectangle:
        def print_class_name:
            print("class name: %s" % cls) # "class name: Rectangle"

References
----------
- `PyLint - R0201 <http://pylint-messages.wikidot.com/messages:r0201>`_
