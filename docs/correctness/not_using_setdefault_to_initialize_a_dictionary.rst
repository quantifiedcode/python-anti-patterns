Not using ``setdefault()`` to initialize a dictionary
=====================================================

Summary
-------

Rather than checking if a key exists in a dictionary via ``if``/``else`` clauses and then creating the key (if it doesn't exist) or setting the key's value (if it already exists), use ``setdefault()``.

Description
-----------

When initializing a dictionary, it is common to see a module check for the existence of a key and then create the key if it does not exist. Although there is nothing wrong with this, the exact same idea can be accomplished more concisely by using the built-in dictionary method ``setdefault()``.

Examples
----------

Using ``if``/``else`` clauses to create and/or set keys
.......................................................

The module below checks if a key named ``list`` exists in a dictionary called ``dictionary``. If it does not exist, then the module creates the key and then sets its value to an empty list. The module then proceeds to append a value to the list.

Although there is nothing wrong with this code, it is unnecessarily verbose. Later you will see how you can use ``setdefault()`` to accomplish the same idea more concisely.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    dictionary = {}

    if not "list" in dictionary:
        dictionary["list"] = []

    dictionary["list"].append["list_item"]

Solutions
---------

Use ``setdefault()`` to initialize a dictionary
...............................................

The modified module below uses ``setdefault()`` to initialize the dictionary. When ``setdefault()`` is called, it will check if the key already exists. If it does exist, then ``setdefault()`` does nothing. If the key does not exist, then ``setdefault()`` creates it and sets it to the value specified in the second argument.

.. code:: python

    dictionary = {}

    list = dictionary.setdefault("list", [])

    list.append("list_item")
    
References
----------
- `Stack Overflow - Use cases for the setdefault dict method <http://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method>`_
