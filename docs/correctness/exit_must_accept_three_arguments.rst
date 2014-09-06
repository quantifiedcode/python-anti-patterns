``__exit__`` must accept 3 arguments: type, value, traceback
============================================================

Summary
-------

The ``__exit__`` method definition for a ``contextmanager`` class must have exactly three arguments. The ``__exit__`` method is called by Python automatically at the end of the code block following a ``with`` statement. Python always passes three arguments to ``__exit__``. Therefore if the user-defined ``__exit__`` method does not define three arguments, a runtime error occurs because the number of arguments provided by Python does not match the number of arguments listed in the method definition.

Description
-----------

A ``contextmanager`` class is any class that implements the ``__enter__`` and ``__exit__`` methods according to the `Python Language Reference's contract <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_. Implementing the ``contextmanager`` contract enables you to use the ``with`` statement with instances of the class. The ``with`` statement is used to ensure that setup and teardown operations are always executed before and after a given block of code. It is functionally equivalent to ``try...finally`` blocks, except that ``with`` statements are more concise.

For example, the following block of code using the ``with`` statement...

.. code:: python

    with EXPRESSION:
        BLOCK
        
... is equivalent to the following block of code using ``try`` and ``finally``.

.. code:: python

    EXPRESSION.__enter__()
    try:
        BLOCK
    finally:
        EXPRESSION.__exit__(exception_type, exception_value, traceback)

In order for ``__exit__`` to work properly it must have exactly three arguments: ``exception_type``, ``exception_value``, and ``traceback``. The formal argument names in the method definition do not need to correspond directly to these names, but they must appear in this order. If any exceptions occur while attempting to execute the block of code nested after the ``with`` statement, Python will pass information about the exception into the ``__exit__`` method. The user can then modify ``__exit__`` to gracefully handle each type of exception.

References
----------
- `PyLint - E0235 <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_
- `Python Language Reference - The with statement <https://docs.python.org/2/reference/compound_stmts.html#with>`_
- `Python Language Reference - With Statement Context Managers <https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers>`_
