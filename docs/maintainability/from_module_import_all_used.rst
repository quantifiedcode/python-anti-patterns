From module import *; unable to detect undefined names
======================================================

Summary
-------

Raised when an import statement is used with the ``*`` wildcard. The ``import`` statement should be refactored to import specific functions and variables if possible.

Description
-----------

When an import statement in the pattern of ``from MODULE import *`` is used it may become difficult for a Python validator to detect undefined names in the program that imported the module. Furthermore, as a general best practice, import statements should be as specific as possible and should only import what they need.

Examples
----------

``From module import *`` statement is used
..........................................

The following code imports everything from the ``math`` built-in Python module.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    from math import *  # wildcard import = bad

Solutions
---------

Make the ``import`` statement more specific
...........................................

The ``import`` statement should be refactored to be more specific about what functions or variables it is using from the ``math`` module. The modified module below specifies exactly which module member it is using, which happens to be ``ceil`` in this example.

.. code:: python

    from math import ceil

References
----------
- PyFlakes - F403
- `Stack Overflow - Importing Modules <http://stackoverflow.com/questions/15145159/importing-modules-how-much-is-too-much>`_

