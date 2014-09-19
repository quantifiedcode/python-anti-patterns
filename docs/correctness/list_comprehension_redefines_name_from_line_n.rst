List comprehension redefines name from line n
=============================================

Summary
-------

A list comprehension is using a name that has already been defined in the module. This can introduce bugs into your module by inadvertently altering the value of variables. Use unique names for list comprehension variables to avoid this potential problem.

Description
-----------

This error is frequently encountered in large modules that use nondescript variable names like ``i``. This is not a critical error per se. A module can still execute when a variable is defined once and then used later on in a list comprehension. However, it is dangerous and is likely to cause bugs. Therefore list comprehensions should be given unique variable names that are not used anywhere else in the module. 

Examples
----------

List comprehension uses variable name defined earlier in module
...............................................................

In the module below, a variable named ``i`` is defined and then used later in a list comprehension. After the list comprehension the value of the ``i`` variable is the value that it was last assigned during the list comprehension, which is ``9`` because of the ``range`` function.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    i = 1
    squares = [i**2 for i in range(10)]
    print squares
    print i  # 9

Solutions
---------

Use a new, unique name in the list comprehension
................................................

The potential problem of inadvertently altering variables is fixed by using unique names in the list comprehension which are not used anywhere else in the module.

.. code:: python

    i = 1
    squares = [item**2 for item in range(10)]
    print squares
    print i  # 1
    
References
----------
- `Python For Beginners <http://www.pythonforbeginners.com/basics/list-comprehensions-in-python>`_
