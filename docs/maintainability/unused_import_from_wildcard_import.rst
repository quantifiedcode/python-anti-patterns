Unused import from wildcard import
==================================

Summary
-------

A wildcard import statement is used in the module, but the module does not use every imported object from the module. The ``unused import from wildcard import`` error is raised for every unused, imported object. To suppress the error replace the wildcard import and explicitly import only the needed objects. Wildcard imports harm code performance and increase the probability of introducing mistakes and bugs into your code.

Description
-----------

`PEP 20, The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_, states that "Explicit is better than implicit." Import statements of the pattern ``from MODULE import OBJECT`` are more explicit than ``from MODULE import *``. Therefore, you should not use wildcard imports but rather should explicitly list which objects you need to use when importing modules. Wildcard imports also make it more difficult for static code analyzers (like this tool) to perform their jobs.

Examples
----------

Wildcard import used, but not all objects used
..............................................

The module below performs a wildcard import on the ``os`` module from the Python Standard Library. However, the module does not use every object from the ``os`` module. It only uses one function, ``getcwd()``. The ``unused import from wildcard import`` is raised for every object from the ``os`` module that is not used.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    from os import *  # creates lots of "unused import from wildcard import" errors

    print "This script is located at {:s}.".format(getcwd())  # getcwd() is the only object from os module being used

Solutions
---------

Replace the wildcard import with explicit imports
.................................................

The modified module below has replaced the wildcard import with explicit imports of only the objects from the ``os`` module which are actually being used. This code is much more explicit than the original, and much less likely to cause problems.

.. code:: python

    from os import getcwd  # MUCH more explicit than the wildcard import

    print "This script is located at {:s}.".format(getcwd())
    
References
----------
- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
- PyLint - W0614
