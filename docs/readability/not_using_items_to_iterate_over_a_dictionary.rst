Not using ``items()`` to iterate over a dictionary
==================================================

Summary
-------

``items()`` is the preferred way to iterate through the key-value pairs of a dictionary. Although there are other valid ways to iterate through a dictionary, this is the most concise way, and you can improve code readability by using the method which is most familiar to the most Python programmers.

Description
-----------

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." The preferred way to iterate over the key-value pairs of a dictionary is to declare two variables in a for loop, and then call ``dictionary.items()``, where ``dictionary`` is the name of your variable representing a dictionary. For each loop iteration, Python will automatically assign the first variable as the key and the second variable as the value for that key.

Examples
----------

For loop does not use ``items()`` to iterate across dictionary
...............................................................

The module below defines a for loop that iterates over a dictionary named ``d``. For each loop iteration Python automatically assigns the value of ``k`` to the name of the next key in the dictionary. Inside of the ``for`` loop the module uses ``k`` to access the value of each key of the dictionary. This is a common way for iterating over a dictionary, but it is not the preferred way in Python.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    dictionary = {"first_name": "Alfred", "last_name":"Hitchcock"}

    for key in dictionary:
        print "%s = %s".format(key, dictionary[key])

Solutions
---------

Use ``items()`` to iterate across dictionary
............................................

The updated module below demonstrates the Pythonic style for iterating through a dictionary. When you define two variables in a ``for`` loop in conjunction with a call to ``items()`` on a dictionary, Python automatically assigns the first variable as the name of a key in that dictionary, and the second variable as the corresponding value for that key.

.. code:: python

    dictionary = {"first_name": "Alfred", "last_name":"Hitchcock"}
    
    for key,value in dictionary.items():
        print "%s = %s".format(key, value)
    
References
----------
- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
