Not using ``iteritems()`` to iterate over a dictionary
======================================================

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

Use ``iteritems()`` to iterate across dictionary
................................................

The updated code below demonstrates the Pythonic style for iterating through a dictionary. When you define two variables in a ``for`` loop in conjunction with a call to ``iteritems()`` on a dictionary, Python automatically assigns the first variable as the name of a key in that dictionary, and the second variable as the corresponding value for that key.

.. code:: python

    d = {"first_name": "Alfred", "last_name":"Hitchcock"}
    
    for key,val in d.iteritems():
        print "{} = {}".format(key, val)

``items()`` may be another choice to iterate a dictionary, but in fact, ``iteritems()`` is better.

In Python 2, Python ``items()`` built a real list of tuples and returned that. That could potentially take a lot of extra memory.

Then, generators were introduced to the language in general, and that method was reimplemented as a iterator-generator method named ``iteritems()``.

In Python 3,the ``iteritems()`` is gone, instead, the ``items()`` returns an iterator just like how ``iteritems()`` works in Python 2.

So if you work with Python 2, ``iteritems()`` is the best choice,and if you work with Python 3, you can only use ``items()``, you have no other choice. 

References
----------

- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
- `What is the difference between dict.items() and dict.iteritems()?     <http://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems>`_
