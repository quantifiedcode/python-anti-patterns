Redefining built-in %r
=================

Summary
-------

Raised when a user-defined module has the same name as a `Python Standard Library built-in module <https://docs.python.org/3/library/>`_. 

Description
-----------



Examples
----------

User-defined module overloads function names from Python Standard Library
.........................................................................

Suppose that you have a module called ``my_math`` that implements a function called ``pow``. The user-defined function ``pow`` prints out a mathematical formula representing a basic exponential expression.

.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """ my_module.py """
    def pow(x, y):
        print("%s ^ %s" % (x, y))

You import the code into your application. The application also uses the ``pow`` function from the Python Standard Library ``math``.

.. code:: python

    from math import pow
    from my_module import pow
    
    pow(2, 3)
    
Which function is called? As it turns out, the user-defined function is called, because it was imported second. If the two import statements were reversed (``from math import pow`` after ``from my_module import pow``) the ``pow` function from the ``math`` module would have been called.

The ambiguous situation demonstrated in the code above explains why it is a bad practice to overload function names that are used in Python Standard Library modules. Overloading names makes your code hard to maintain and hard to read, and can cause subtle bugs when the wrong function is called.


    

Solutions
---------

Rename the overloaded function 
..............................



.. code:: python

    
References
----------
- `URL Description <URL>`_
