Unreachable code
================

Summary
-------

Within a function or method there is code after a ``return`` or ``raise`` statement. Code after a ``return`` or ``raise`` statement is never executed. This can cause serious bugs in a program if any part of the program relies on that code.

Description
-----------

When a function or method calls ``return`` or ``raise``, processing for that function or method stops and control is returned to the code that called the function. Any code that is placed after a ``return`` or ``raise`` statement will never be executed. If any part of the program could potentially rely on this code, then the code must be moved to a location where it can be reached. If the code is unnecessary, then it should be removed, because extra code reduces readability.

Examples
----------

Code placed after ``return`` statement
........................................

When a new ``Rectangle`` object is created, the instance member ``area`` is supposed to be initialized and the value of ``area`` printed to standard output. However, because this code is placed after a ``return`` statement, ``area`` is never initialized to its correct value or printed. Subsequent calls to methods that rely on ``area`` will yield incorrect values (since ``area`` was never properly initialized) or result in undefined behavior (i.e. bugs).

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            return
            self.area = width * height # never executed
            print self.area # never executed
    def area(self):
        return self.area # possibly undefined
        
    r = Rectangle(5, 12)
    r.area() # undefined
            
Solutions
-----------

Move necessary code before the ``return`` statement
..............................................

Initializing the value of ``area`` is important to the correct operation of the class, so the code for initializing ``area`` is moved in front of the ``return`` statement in ``__init__``.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height # moved in front of return
            print self.area # moved in front of return, optional
            return

Remove unnecessary code
...........................

The owner of the ``Rectangle`` class determined that printing the value of ``area`` was unnecssary, so this code was removed. In general, unnecessary code should be removed because it reduces readability.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height # moved in front of return
            return
            # removed "print self.area"

References
----------
- `PyLint - W0101 <http://pylint-messages.wikidot.com/messages:w0101>`_
