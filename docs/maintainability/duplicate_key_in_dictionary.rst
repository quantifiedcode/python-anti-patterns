Duplicate key in dictionary
===========================

Summary
-------

A key occurs multiple times in a dictionary. When a key is duplicated, the last definition of the key overwrites previous definitions of the key. Remove the duplicate key from the dictionary, as this could potentially create bugs in the future.

Description
-----------

Python does not detect that duplicate keys have been defined in a dictionary. Whenever it encounters a redefinition of a key, it just overwrites the key's value. Because this has strong potential to create strange and hard to track bugs, you should review the dictionary and delete all duplicate key definitions.

Examples
----------

Duplicate keys in dictionary
............................

In the module below the ``gmt`` key has been defined twice. When you print out the ``time`` variable, note the value of ``gmt``. It corresponds to the last definition for ``gmt``. Python silently wrote over the previous value of ``-08`` for the ``gmt`` key.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    time = {"gmt": -08, "hour": 16, "minute": 37, "second": 05, "gmt": -09}
    print time  # {'second': 05, 'minute': 37, 'hour': 16, 'gmt': -09}

Solutions
---------

Delete duplicate keys
.....................

In the modified module below the second, duplicate entry for ``gmt`` has been deleted.

.. code:: python

    time = {"gmt": -08, "hour": 16, "minute": 37, "second": 05}
    print time  # {'second': 05, 'minute': 37, 'hour': 16, 'gmt': -08}

References
----------
- PyLint - W0109
