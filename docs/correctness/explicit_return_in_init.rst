Explicit return in __init__
===========================

Summary
-------

The ``__init__`` operation contains a ``return`` statement that returns a value other than ``None``.

Description
-----------

``__init__`` is a `special Python method <https://docs.python.org/2/reference/datamodel.html#special-method-names>`_. It is automatically called when a class instance is first created. ``__init__`` should only be used to initialize the values of the new class instance. The ``Explicit return in __init__`` error is raised whenever an ``__init__`` method returns any value other than ``None``.

Examples
----------

The ``__init__`` method of the ``Rectangle`` class below attempts to return the area of the rectangle within the ``__init__`` method. This will cause the ``Explicit return in __init__`` error because Python does not allow an ``__init__`` statement to return any value other than ``None``.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
            return self.area

Solutions
-----------

Remove the `return` statement from the ``__init__`` method
..........................................................

Remove the ``return`` statement in the ``__init__`` method that is returning a value.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height

References
----------
- `PyLint - E0101 <http://pylint-messages.wikidot.com/messages:e0101>`_
- `Python Language Reference - object.__init__(self[, ...]) <https://docs.python.org/2/reference/datamodel.html#object.__init__>`_
