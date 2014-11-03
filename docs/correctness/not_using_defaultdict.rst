Not using ``defaultdict()``
===========================

Summary
-------

Rather than using ``if`` statements or ``for`` loops to initialize the keys of a dict, use the Python Standard Library built-in method ``defaultdict()`` to automatically initialize the value of every key in the dict. Using ``defaultdict()`` is more concise and less error-prone, as the programmer no longer has to remember to manually initialize the value of every key.

Description
-----------

When a dict is created using ``defaultdict()``, the value for each key in the dict will default to the value provided as the first argument of ``defaultdict()``. This is more concise and less error-prone than manually setting the value of each key.

Examples
----------

Manually initializing the keys of a dict
........................................

The module below defines an empty dict and then manually initializes the keys of the dict. Although there is nothing wrong with this code, there is a more concise and less error-prone way to achieve the same idea, as explained in the solution below.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    d = {}

    if not "k" in d:
        d["k"] = 6

    d["k"] += 1

    print d["k"]  # 7

Solutions
---------

Use ``defaultdict()`` to initialize dict keys
.............................................

The modified module below uses ``defaultdict`` to initialize the dict. Whenever a new key is created, the default value for that key is 6. This module is functionally equivalent to the previous module, but this one is more concise and less error-prone, because every key automatically initializes to 6 with no work on the part of the programmer.

.. code:: python

    from collections import defaultdict

    d = defaultdict(lambda : 6)
    d["k"] += 1

    print d["k"]  # 7

References
----------
- `Python Standard Library - collections.defaultdict <https://docs.python.org/2/library/collections.html#collections.defaultdict>`_
