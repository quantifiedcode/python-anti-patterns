Not using ``items()`` to iterate over a dictionary
==================================================

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." The preferred way to iterate over the key-value pairs of a dictionary is to declare two variables in a for loop, and then call ``dictionary.items()``, where ``dictionary`` is the name of your variable representing a dictionary. For each loop iteration, Python will automatically assign the first variable as the key and the second variable as the value for that key.

Anti-pattern
------------

The code below defines a for loop that iterates over a dictionary named ``d``. For each loop iteration Python automatically assigns the value of ``key`` to the name of the next key in the dictionary. Inside of the ``for`` loop the code uses ``key`` to access the value of each key of the dictionary. This is a common way for iterating over a dictionary, but it is not the preferred way in Python.

.. code:: python

    d = {"first_name": "Alfred", "last_name":"Hitchcock"}

    for key in d:
        print("{} = {}".format(key, d[key]))

Best-practice
-------------

Use ``items()`` to iterate across dictionary
............................................

The updated code below demonstrates the Pythonic style for iterating through a dictionary. When you define two variables in a ``for`` loop in conjunction with a call to ``items()`` on a dictionary, Python automatically assigns the first variable as the name of a key in that dictionary, and the second variable as the corresponding value for that key.

.. code:: python

    d = {"first_name": "Alfred", "last_name":"Hitchcock"}

    for key,val in d.items():
        print("{} = {}".format(key, val))

Difference Python 2 and Python 3
--------------------------------

In python 2.x the above examples using ``items`` would return a list with tuples containing the copied key-value pairs of the dictionary. In order to not copy and with that load the whole dictionary's keys and values inside a list to the memory you should prefer the ``iteritems`` method which simply returns an iterator instead of a list.
In Python 3.x the ``iteritems`` is removed and the ``items`` method returns view objects. The benefit of these view objects compared to the tuples containing copies is that every change made to the dictionary is reflected in the view objects.

References
----------

- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
- `Python 2 dict.iteritems <https://docs.python.org/2/library/stdtypes.html#dict.iteritems>`_
- `Python 3 dict.items <https://docs.python.org/3.3/library/stdtypes.html#dict-views>`_


Status
------

- No automated check available. `Create it <https://www.quantifiedcode.com/app/patterns>`_ with `Cody <http://docs.quantifiedcode.com/patterns/language/index.html>`_.

