Not using ``defaultdict()``
===========================

When a dict is created using ``defaultdict()``, the value for each key in the dict will default to the value provided as the first argument of ``defaultdict()``. This is more concise and less error-prone than manually setting the value of each key.

Anti-pattern
------------

The code below defines an empty dict and then manually initializes the keys of the dict. Although there is nothing wrong with this code, there is a more concise and less error-prone way to achieve the same idea, as explained in the solution below.

.. code:: python

    d = {}

    if not "k" in d:
        d["k"] = 6

    d["k"] += 1

    print d["k"]  # 7

Best practice
-------------

Use ``defaultdict()`` to initialize dict keys
.............................................

The modified code below uses ``defaultdict`` to initialize the dict. Whenever a new key is created, the default value for that key is 6. This code is functionally equivalent to the previous code, but this one is more concise and less error-prone, because every key automatically initializes to 6 with no work on the part of the programmer.

.. code:: python

    from collections import defaultdict

    d = defaultdict(lambda : 6)
    d["k"] += 1

    print d["k"]  # 7

References
----------

- `Python Standard Library - collections.defaultdict <https://docs.python.org/2/library/collections.html#collections.defaultdict>`_
