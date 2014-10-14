Redefining name from outer scope
================================

Summary
-------

A function, class, or control structure (for loop, while loop, etc.) has redefined a name that has already been defined outside of its scope. This creates confusing code because the same name is being used to refer to different things. It also prevents the local scope code from being able to access the global scope name. If the module attempted to import the global name and use it within the local scope, Python would raise a ``SyntaxError`` and the module would not successfully execute. Give the outer scope name and inner scope name different names to prevent this naming conflict.

Description
-----------

Using the same name for multiple, different variables creates confusing code. It also prevents the local scope code from being able to access the global scope name. Therefore, you should give rename the conflicting global and local names to different, unique names.

Examples
----------

Name defined at global and local scope
......................................

The name ``n`` is defined as both a parameter name for ``get_random_number()`` as well as a global variable. In addition to being confusing code, when ``get_random_number()`` attempts to access the global name ``n`` Python raises a ``SyntaxError`` and aborts execution. This is because Python would not be able to resolve which ``n`` was being referred to for every subsequent reference to ``n`` within ``get_random_number()``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import math
    import random

    def get_random_number(n):  # local scope definition of n
        global n  # n is both global and local now... bad!
        return int(math.floor(random.random() * n))  # SyntaxError. Is this the parameter n or the global n?!?

    n = 5  # n defined here at global scope

    print "n at global scope equals {:d}".format(n)

    get_random_number(5)  # SyntaxError: name 'n' is local and global

Solutions
---------

Rename the conflicting names
............................

The ``redefining name from outer scope`` error can be suppressed by renaming the conflicting names to unique values. In the modified module below the parameter name for ``get_random_number()`` has been renamed from ``n`` to ``multiplier``. Now the name ``n`` only refers to the global variable, so there is no more naming conflict and the module executes successfully.

.. code:: python

    import math
    import random

    def get_random_number(multiplier):  # renamed parameter from n to multiplier
        global n  # n uniquely refers to global variable now
        print "n inside of get_random_number equals {:d}".format(n)
        return int(math.floor(random.random() * multiplier))

    n = 5 

    print "n at global scope equals {:d}".format(n)

    get_random_number(5)  # ok now
    
References
----------
- PyLint - W0621
