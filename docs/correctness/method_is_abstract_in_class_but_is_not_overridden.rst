Method is abstract in class but is not overridden
=================================================

Summary
-------

A child class has not implemetend one of the abstract methods that it inherited from its parent class. Implement the method as a concrete method in the child class or else Python will raise a ``TypeError`` and the module will not be able to successfully execute.

Description
-----------

Abstract methods are implemented using the ``abc`` module from the Python Standard Library. When a method is designed as abstract in a parent class (via the method decorator ``abc.abstractmethod``) and the child class does not implement the method, then the ``method is abstract in class but is not overridden`` error will be raised. Python will raise a ``TypeError`` error at runtime if you attempt to instantiate any object that contains abstract methods.

Examples
----------

Child class does not implement abstract method
..............................................

The ``Square`` class in the module below inherits an abstract method called ``area()`` from its parent class ``Rectangle``, but ``Square`` does not implement the method. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import abc

    class Rectangle(object):
        __metaclass__ = abc.ABCMeta

        def __init__(self, width, height):
            self.width = width
            self.height = height

        @abc.abstractmethod
        def area(self):
            return

    class Square(Rectangle):
        def __init__(self, length):
            super(Square, self).__init__(length, length)

    s = Square(5)  # TypeError: can't instantiate abstract class


Solutions
---------

Implement the abstract method
.............................

In the modified module below, the ``Square`` class has concretely implemented the ``area()`` method and the ``method is abstract in class but is not overridden`` error is no longer valid.

.. code:: python

    import abc

    class Rectangle(object):
        __metaclass__ = abc.ABCMeta

        def __init__(self, width, height):
            self.width = width
            self.height = height

        @abc.abstractmethod
        def area(self):
            return

    class Square(Rectangle):
        def __init__(self, length):
            super(Square, self).__init__(length, length)
        def area(self):
            return self.width * self.height

    s = Square(5)

References
----------
- `Stack Overflow - Abstract Methods in Python <http://stackoverflow.com/questions/4382945/abstract-methods-in-python>`_
