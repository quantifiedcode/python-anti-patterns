using wildcard imports (`from ... import *`)
============================================

When an import statement in the pattern of ``from MODULE import *`` is used it may become difficult for a Python validator to detect undefined names in the program that imported the module. Furthermore, as a general best practice, import statements should be as specific as possible and should only import what they need.

Anti-pattern
------------

The following code imports everything from the ``math`` built-in Python module.

.. code:: python

    from math import *  # wildcard import = bad

Best practices
--------------

Make the ``import`` statement more specific
...........................................

The ``import`` statement should be refactored to be more specific about what functions or variables it is using from the ``math`` module. The modified code below specifies exactly which module member it is using, which happens to be ``ceil`` in this example.

.. code:: python

    from math import ceil

Import the whole module
.......................

There are some cases where making the ``import`` statement specific is not a good solution:

- It may be unpractical or cumbersome to create or maintain the list of objects to be imported from a module
- A direct import would bind to the same name as that of another object (e.g. from asyncio import TimeoutError)
- The module that the object is imported from would provide valuable contextual information if it is right next to the object when it's used.

In these cases, use one of these idioms:

.. code:: python

    import math
    x = math.ceil(y)

    # or

    import multiprocessing as mp
    pool = mp.pool(8)


References
----------

- PyFlakes - F403
- `Stack Overflow - Importing Modules <http://stackoverflow.com/questions/15145159/importing-modules-how-much-is-too-much>`_
- `Stack Overflow - 'import module' or 'from module import' <http://stackoverflow.com/questions/710551/import-module-or-from-module-import>`_

