Class has no member
===================

Summary
-------

A module is attempting to use an undefined member of a class. Implement the member or remove the statement referencing the undefined member or else Python will raise a runtime error and the module will not execute.

Description
-----------

When a module attempts to use a member of a class which is not defined in that class, Python raises an ``AttributeError`` and stops executing the program. Either implement the undefined member or remove the statement referencing the undefined member or else the module will not be able to execute successfully.

Examples
----------

Description of error
....................

The module below attempts to call a function from the ``Rectangle`` class called ``area``. This raises the ``class has no member`` error because the ``area`` function in undefined in the ``Rectangle`` class. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r = Rectangle(5, 4)

    print r.area()  # no such member in Rectangle class


Solutions
---------

Implement the undefined member
..............................

The updated module below implements the ``area`` member. Now that the function is defined, the ``class has no member`` error is suppressed.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area():
            return self.width * self.height

    r = Rectangle(5, 4)

    print r.area()  # ok now

Remove the reference to the undefined member
............................................

The updated module below suppresses the ``class has no member`` error by using known defined class members to work around the problem. Rather than trying to use the undefined member ``area``, the module multiples the ``width`` and ``height`` attributes of the instance to get the desired value.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area():
            return self.width * self.height

    r = Rectangle(5, 4)

    area = r.width * r.height  # using known members to get the desired value

    print area

References
----------
- Pylint - E1101
