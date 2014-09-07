Using the ``global`` statement
==============================

Summary
-------

The ``global`` statement was encountered. Global variables reduce code readability and often cause bugs. They should be avoided as much as possible.

Description
-----------

Global variables are dangerous because they can be simultaneously accessed from multiple sections of a program. This frequently results in bugs. Most bugs involving global variables arise from one function reading and acting on the value of a global variable before another function has the chance to set it to an appropriate value.

Global variables also make code difficult to read, because they force you to search through multiple functions or even modules just to understand all the different locations where the global variable is used and modified.

Examples
----------

Module and functions use ``global`` statement
.............................................

The module below uses global variables and a function to compute the area and perimeter of a rectangle. As you can see, even with two functions it becomes difficult to keep track of how the global variables are used and modified.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    WIDTH = 0 # global variable
    HEIGHT = 0 # global variable

    def area(w, h):
        global WIDTH # global statement
        global HEIGHT # global statement
        WIDTH = w
        HEIGHT = h
        return WIDTH * HEIGHT
        
    def perimeter(w, h):
        global WIDTH # global statement
        global HEIGHT # global statement
        WIDTH = w
        HEIGHT = h
        return ((WIDTH * 2) + (HEIGHT * 2))        

    print "WIDTH:" , WIDTH # "WIDTH: 0"
    print "HEIGHT:" , HEIGHT # "HEIGHT: 0"

    print "area():" , area(3, 4) # "area(): 12"

    print "WIDTH:" , WIDTH # "WIDTH: 3"
    print "HEIGHT:" , HEIGHT # "HEIGHT: 4"


Solutions
---------

Encapsulate the global variables into objects
.............................................

One common solution for avoiding global variables is to create a class and store related global variables as members of an instantiated object of that class. This results in more compact and safer code.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            return self.area
        def area(self):
            return self.width * self.height
        def circumference(self):
            return ((self.width * 2) + (self.height * 2))
            
    r = Rectangle(3, 4)        
    print "area():" , r.area()
    
References
----------
- `Cunningham & Cunningham, Inc. - Global Variables Are Bad <http://c2.com/cgi/wiki?GlobalVariablesAreBad>`_
