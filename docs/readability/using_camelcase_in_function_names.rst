Using `CamelCase` in function names
===================================

Per the PEP 8 Style Guide, function names should be lowercase, with words separated by underscores.


Anti-pattern
------------

.. code:: python

    def someFunction():
        print "Is not the preferred PEP 8 pattern for function names"

Best practice
-------------

Using lowercase with underscores
................................

The code below uses the PEP 8 preferred pattern of function names.

.. code:: python

    def some_function():
        print "PEP 8 Style Guide prefers this pattern"

References
----------
- `PEP8 Style Guide - Function names <https://www.python.org/dev/peps/pep-0008/#function-names>`_
