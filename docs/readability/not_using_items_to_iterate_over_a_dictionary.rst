Not using ``items()`` to iterate over a dictionary
==================================================

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." The preferred way to iterate over the key-value pairs of a dictionary is to declare two variables in a for loop, and then call ``dictionary.items()``, where ``dictionary`` is the name of your variable representing a dictionary. For each loop iteration, Python will automatically assign the first variable as the key and the second variable as the value for that key.

Anti-pattern
------------

The code below defines a for loop that iterates over a dictionary named ``d``. For each loop iteration Python automatically assigns the value of ``key`` to the name of the next key in the dictionary. Inside of the ``for`` loop the code uses ``key`` to access the value of each key of the dictionary. This is a common way for iterating over a dictionary, but it is not the preferred way in Python.

.. code:: python

    d = {"first_name": "Alfred", "last_name":"Hitchcock"}

    for key in d:
        print "{} = {}".format(key, d[key])

Best-practice
-------------

Use ``items()`` to iterate across dictionary
............................................

The updated code below demonstrates the Pythonic style for iterating through a dictionary. When you define two variables in a ``for`` loop in conjunction with a call to ``items()`` on a dictionary, Python automatically assigns the first variable as the name of a key in that dictionary, and the second variable as the corresponding value for that key.

.. code:: python

    d = {"first_name": "Alfred", "last_name":"Hitchcock"}
    
    for key,val in d.items():
        print "{} = {}".format(key, val)

References
----------

- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
