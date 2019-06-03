Explicit return in __init__
===========================

``__init__`` is a `special Python method <https://docs.python.org/2/reference/datamodel.html#special-method-names>`_ that is automatically called when memory is allocated for a new object. The sole purpose of ``__init__`` is to initialize the values of instance members for the new object. Using ``__init__`` to return a value implies that a program is using ``__init__`` to do something other than initialize the object. This logic should be moved to another instance method and called by the program later, after initialization.

Anti-pattern
------------

The ``__init__`` method of the ``Rectangle`` class below attempts to return the area of the rectangle within the ``__init__`` method. This violates the rule of only using ``__init__`` to initialize instance members.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
            # causes "Explicit return in __init__" error
            return self.area

Best practices
--------------

Remove the `return` statement from the ``__init__`` method
..........................................................

Remove the ``return`` statement in the ``__init__`` method that is returning a value.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
            # return statement removed from here

Move the program logic to another instance method
.................................................

There is no reason why the ``Rectangle`` class MUST return the area immediately upon initialization. This program logic should be moved to a separate method of the ``Rectangle`` class. The program can call the method later, after the object has successfully initialized.

Note that even if you set the return value, but Python will just ignore the returned value.

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self._area = width * height

        @property
        # moved the logic for returning area to a separate method
        def area(self):
            return self._area

Note that the class must inherit from ``object`` now, since the ``property`` decorator only works for new style classes.

References
----------

- PyLint - E0101, return-in-init
- `Python Language Reference - object.__init__(self[, ...]) <https://docs.python.org/2/reference/datamodel.html#object.__init__>`_



