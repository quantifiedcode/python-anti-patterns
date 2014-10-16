Wildcard import
===============

Summary
-------

The wildcard ``*`` was used in an import statement. Wildcard imports import all public objects from the imported module. This can potentially create bugs when a name from the imported module is the same as name from your module. Therefore the wildcard should be avoided to improve maintainability.

Description
-----------

Use qualified names rather than wildcard imports. For example, rather than using the wildcard import statement ``from math import *`` to use the ``floor`` function from the ``math`` module, import the module (e.g. ``import math``) and then use the qualified name of the function (e.g. ``math.floor``). This eliminates the possibility of accidentally using the wrong name.

Examples
----------

Wildcard import used
....................

The module below imports the ``math`` module from the Python standard library. This library contains a function called ``floor``. The function also defines a function with the same name. When this module is executed, either ``floor`` function could potentially be called. This is especially dangerous if the module attempts to use the value returned by the function anywhere else in the module. In the example below, the module presumably is attempting to call ``math.floor`` to round down the integer supplied as an argument. However, because the module's ``floor`` function was defined after the import, it overrides the ``math.floor`` function. Since a function returns ``None`` by default when no return statement is defined, the ``floor`` function returns ``None``. This causes a ``TypeError`` at runtime when Python attempts to divide ``10`` by ``x``, which equals ``None``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    from math import *

    def floor(n):
        print "floor:", n

    x = floor(5.3)  # dangerous situation: what is the value of x?

    10 / x  # causes TypeError, because x is None!

Solutions
---------

Remove the wildcard import and use qualified names
..................................................

Wildcard imports should be avoided as much as possible and replaced with qualified names. In the modified example below, the wildcard import ``from math import *`` has been replaced with ``import math``, and the ``floor`` function from the ``math`` module is fully qualified before it is used. This eliminates the possibility of calling the wrong ``floor`` function.

.. code:: python

    import math  # removed the wildcard

    def floor(n):
        print "floor:", n

    x = math.floor(5.3)  # no ambiguity
    
    10 / x  # ok now

References
----------
- `Stack Overflow - Should wildcard import be avoided? <http://stackoverflow.com/questions/3615125/should-wildcard-import-be-avoided>`_
- `PEP8 Style Guide - Imports <http://legacy.python.org/dev/peps/pep-0008/#imports>`_
- PyLint - W0401
