Redefining built-in %r
======================

Summary
-------

Raised when the function in a user-defined module has the same name as a `Python Standard Library built-in module function <https://docs.python.org/3/library/>`_. Overloading function names makes your code hard to maintain and hard to read, and can cause subtle bugs when the wrong function is called.

Description
-----------

When a user-defined function has the same name as a function from a Python Standard Library, the ``Redefining built-in %r`` error is raised, where ``%r`` is the name of the function that is being overloaded with two or more names. Overloading functions is generally a bad programming practice and should be avoided at all costs.

Examples
----------

User-defined module overloads function names from Python Standard Library
.........................................................................

The ``my_math`` module below implements a function called ``pow``. ``pow`` prints out a mathematical formula representing a basic exponential expression.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """ my_module.py """
    def pow(x, y):
        print("%s ^ %s" % (x, y))

An application imports this module, in addition to the Python Standard Library's ``math`` module. ``math`` also implements a function named ``pow`` which returns the product of ``x`` raised to the power of ``y``.

.. code:: python

    from math import pow
    from my_module import pow
    
    pow(2, 3)
    
Which function is called? The user-defined ``pow`` is called, because it was imported last. If the two import statements were reversed (``from math import pow`` after ``from my_module import pow``) the ``pow`` function from the ``math`` module would have been called.

This ambiguous situation demonstrates why it is a bad practice to overload function names that are used in Python Standard Library modules. Overloading names makes your code hard to maintain and hard to read, and can cause subtle bugs when the wrong function is called.

Solutions
---------

Rename the overloaded function 
..............................

Rename the user-defined function to a name that is not used by any Python Standard Library module.

.. code:: python

    """ my_module.py """
    def print_pow(x, y): # changed from pow to print_pow
        print("%s ^ %s" % (x, y))

Explicitly reference the module
...............................

Explicitly reference each function by module. 

.. code:: python

    from math import pow
    from my_module import pow
    
    my_module.pow(2, 3) # prints "2 ^ 3"
    math.pow(2, 3) # returns 8

    
References
----------
- `Stack Overflow - Module name redefines built-in <http://stackoverflow.com/questions/3639511/module-name-redefines-built-in>`_
- PyLint - W0622
