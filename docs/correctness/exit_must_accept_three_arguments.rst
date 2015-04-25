``__exit__`` must accept 3 arguments: type, value, traceback
============================================================

A ``contextmanager`` class is any class that implements the ``__enter__`` and ``__exit__`` methods according to the `Python Language Reference's context management protocol <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_. Implementing the context management protocol enables you to use the ``with`` statement with instances of the class. The ``with`` statement is used to ensure that setup and teardown operations are always executed before and after a given block of code. It is functionally equivalent to ``try...finally`` blocks, except that ``with`` statements are more concise.

For example, the following block of code using a ``with`` statement...

.. code:: python

    with EXPRESSION:
        BLOCK

... is equivalent to the following block of code using ``try`` and ``finally`` statements.

.. code:: python

    EXPRESSION.__enter__()
    try:
        BLOCK
    finally:
        EXPRESSION.__exit__(exception_type, exception_value, traceback)

In order for ``__exit__`` to work properly it must have exactly three arguments: ``exception_type``, ``exception_value``, and ``traceback``. The formal argument names in the method definition do not need to correspond directly to these names, but they must appear in this order. If any exceptions occur while attempting to execute the block of code nested after the ``with`` statement, Python will pass information about the exception into the ``__exit__`` method. You can then modify the definition of ``__exit__`` to gracefully handle each type of exception.

Anti-pattern
------------

The ``__exit__`` method defined in the ``Rectangle`` class below does not conform to Python's context management protocol. The method is supposed to take four arguments: ``self``, exception type, exception value, and traceback. Because the method signature does not match what Python expects, ``__exit__`` is never called even though it should have been, because the method ``divide_by_zero`` creates a ``ZeroDivisionError`` exception.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def __enter__(self):
            print "in __enter__"
            return self
        def __exit__(self): # never called because
                            # argument signature is wrong
            print "in __exit__"
        def divide_by_zero(self): # causes ZeroDivisionError exception
            return self.width / 0

    with Rectangle(3, 4) as r:
        r.divide_by_zero() # __exit__ should be called but isn't

    # Output:
    # "in __enter__"
    # Traceback (most recent call last):
    #   File "e0235.py", line 27, in <module>
    #     r.divide_by_zero()
    # TypeError: __exit__() takes exactly 1 argument (4 given)

Best practices
--------------

Modifying ``__exit__`` to accept four arguments ensures that ``__exit__`` is properly called when an exception is raised in the indented block of code following the ``with`` statement. Note that the argument names do not have to exactly match the names provided below. But they must occur in the order provided below.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def __enter__(self):
            print "in __enter__"
            return self
        def __exit__(self, exception_type, exception_value, traceback):
            print "in __exit__"
        def divide_by_zero(self): # causes ZeroDivisionError exception
            return self.width / 0

    with Rectangle(3, 4) as r:
        r.divide_by_zero() # exception successfully pass to __exit__

    # Output:
    # "in __enter__"
    # "in __exit__"
    # Traceback (most recent call last):
    #   File "e0235.py", line 27, in <module>
    #     r.divide_by_zero()

References
----------

- `PyLint - E0235 <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_
- `Python Language Reference - The with statement <https://docs.python.org/2/reference/compound_stmts.html#with>`_
- `Python Language Reference - With Statement Context Managers <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_
- `Stack Overflow - Python with...as <http://stackoverflow.com/a/14776885/1669860>`_
