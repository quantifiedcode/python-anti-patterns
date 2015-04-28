Not using ``get()`` to return a default value from a dict
=========================================================

Frequently you will see a code create a variable, assign a default value to the variable, and then check a dict for a certain key. If the key exists, then the value of the key is copied into the value for the variable. While there is nothing wrong this, it is more concise to use the built-in method ``dict.get(key[, default])`` from the Python Standard Library. If the key exists in the dict, then the value for that key is returned. If it does not exist, then the default value specified as the second argument to ``get()`` is returned. Note that the default value defaults to ``None`` if a second argument is not provided.

Anti-pattern
------------

The code below initializes a variable called ``data`` to an empty string. Then it checks if a certain key called ``message`` exists in a dict called ``dictionary``. If the key exists, then the value of that key is copied into the ``data`` variable.

Although there is nothing wrong with this code, it is verbose. The solution below demonstrates how express the same idea in a more concise manner by using ``dict.get(key[, default])``.

.. code:: python

    dictionary = {"message": "Hello, World!"}

    data = ""

    if "message" in dictionary:
        data = dictionary["message"]

    print data  # Hello, World!

Best practice
-------------

Use ``dict.get(key[, default])`` to assign default values
.........................................................

The code below is functionally equivalent to the original code above, but this solution is more concise.

When ``get()`` is called, Python checks if the specified key exists in the dict. If it does, then ``get()`` returns the value of that key. If the key does not exist, then ``get()`` returns the value specified in the second argument to ``get()``.

.. code:: python

    dictionary = {"message": "Hello, World!"}

    data = dictionary.get("message", "")

    print data  # Hello, World!

References
----------

- `Python Standard Library - dict.get <https://docs.python.org/2/library/stdtypes.html#dict.get>`_
