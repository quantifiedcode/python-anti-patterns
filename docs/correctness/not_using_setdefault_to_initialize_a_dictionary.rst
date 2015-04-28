Not using ``setdefault()`` to initialize a dictionary
=====================================================

When initializing a dictionary, it is common to see a code check for the existence of a key and then create the key if it does not exist. Although there is nothing wrong with this, the exact same idea can be accomplished more concisely by using the built-in dictionary method ``setdefault()``.

Anti-pattern
------------

The code below checks if a key named ``list`` exists in a dictionary called ``dictionary``. If it does not exist, then the code creates the key and then sets its value to an empty list. The code then proceeds to append a value to the list.

Although there is nothing wrong with this code, it is unnecessarily verbose. Later you will see how you can use ``setdefault()`` to accomplish the same idea more concisely.

.. code:: python

    dictionary = {}

    if "list" not in dictionary:
        dictionary["list"] = []

    dictionary["list"].append["list_item"]

Best practice
-------------

Use ``setdefault()`` to initialize a dictionary
...............................................

The modified code below uses ``setdefault()`` to initialize the dictionary. When ``setdefault()`` is called, it will check if the key already exists. If it does exist, then ``setdefault()`` does nothing. If the key does not exist, then ``setdefault()`` creates it and sets it to the value specified in the second argument.

.. code:: python

    dictionary = {}

    dictionary.setdefault("list", []).append("list_item")

References
----------

- `Stack Overflow - Use cases for the setdefault dict method <http://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method>`_
