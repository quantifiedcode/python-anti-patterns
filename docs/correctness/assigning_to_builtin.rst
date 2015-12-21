Assigning to built-in function
==============================

Python has a number of built-in functions that are always accessible in the interpreter. Unless you have a special reason, you should neither overwrite these functions nor assign a value to a variable that has the same name as a built-in function. Overwriting a built-in might have undesired side effects or can cause runtime errors. Python developers usually use built-ins 'as-is'. If their behaviour is changed, it can be very tricky to trace back the actual error.

Anti-pattern
------------

In the code below, the ``list`` built-in is overwritten. This makes it impossible, to use ``list`` to define a variable as a list. As this is a very concise example, it is easy to spot what the problem is. However, if there are hundreds of lines between the assignment to ``list`` and the assignment to ``cars``, it might become difficult to identify the problem.

.. code:: python

    # Overwriting built-in 'list' by assigning values to a variable called 'list'
    list = [1, 2, 3]
    # Defining a list 'cars', will now raise an error
    cars = list()
    # Error: TypeError: 'list' object is not callable

Best practice
-------------

Unless you have a very specific reason to use variable names that have the same name as built-in functions, it is recommended to use a variable name that does not interfere with built-in function names.

.. code:: python

    # Numbers used as variable name instead of 'list'
    numbers = [1, 2, 3]
    # Defining 'cars' as list, will work just fine
    cars = list()

References
----------
- `Python Documentation: Built-in functions <https://docs.python.org/2/library/functions.html>`_


Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/8ae91093b4f2420f8eac5cc826470aec>`_
