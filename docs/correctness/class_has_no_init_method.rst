Class has no ``__init__`` method
================================

Summary
-------

No ``__init__`` method has been defined for a class. Treat this as a warning and check that the class in question is fully implemented. If the class truly requires no initialization, consider creating an empty ``__init__`` method to suppress this error and to explicitly indicate that no initialization is needed.

Description
-----------

Although a class can function without an ``__init__`` method, it is unusual for a class not to require any initialization whatsoever. When you encounter this error you should check the class in question to see if any initialization routines have been forgotten about.

Examples
--------

No ``__init__`` method defined
..............................

The ``Car`` class triggers the ``class has no __init__ method`` warning because it has not implemented an ``__init__`` method.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Car:  # class defines no __init__ method
        def print_class_name(self):
            print "Car"

    c = Car()
    c.print_class_name()


Solutions
---------

Implement an ``__init__`` method
................................

Upon reviewing the code, the author created an empty ``__init__`` method to explicitly indicate to other programmers that the ``Car`` class requires no initialization.

.. code:: python

    class Car:
        def __init__(self):
        """N/A"""
        def print_class_name(self):
            print "Car"

    # ...

References
----------
- Pylint - W0232
