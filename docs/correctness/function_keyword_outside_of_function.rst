Function keyword outside of function
====================================

Summary
-------

The keywords ``yield`` or ``return`` were used outside of a function. These keywords are only valid inside of functions. Remove the statement or wrap it inside of a function or else Python will raise a ``SyntaxError`` and the module will not execute.

Description
-----------

This article is generally applicable to the two errors ``Yield outside function`` and ``Return outside function``. Both errors are indicating the same general problem: a keyword that is only allowed inside of functions is being used outside of a function. The only solution to this error is to either remove the statement, or to wrap it inside of a function.

Examples
--------

``return`` used outside of function
...................................

The module below is frequently imported into other modules. The author is trying to generate a random value and return this value to the other modules that import it. The author mistakenly believes that using a ``return`` statement at the global level of this module will accomplish this functionality. In reality Python does not allow this. The ``return`` keyword can only be used inside of functions. Python will raise a ``SyntaxError`` and the module will not execute successfully.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """random_nums.py"""
    import random

    r = random.random()

    print "Your random number is", r

    return r  # SyntaxError: return outside function

``yield`` used outside of function
...................................

The author of the module below is new to Python and does not understand how ``yield`` is used. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    for n in range(10):
        yield n

Solutions
---------

Remove the ``return`` statement
...............................

The modified module below suppresses the ``return outside function`` by deleting the return statement.

.. code:: python

    """random_nums.py"""
    import random

    r = random.random()

    print "Your random number is", r

    # deleted return statement here

Wrap the ``return`` statement in a function
...........................................

The modified module below suppresses the ``return outside function`` by wrapping the ``return`` statement inside of a function. Whenever another module imports this module and wants to get a random number, the other module can just call ``import random_nums`` and then call ``random_nums.get_random_number()``.

.. code:: python

    """random_nums.py"""
    import random

    def get_random_number():
        r = random.random()
        print "Your random number is", r
        return r  # wrapped up the return statement inside of a function

Remove the ``yield`` statement
..............................

The modified module below suppresses the ``yield outside function`` by replacing the ``yield`` statement with a ``print`` statement. This is just an example, the solution will depend on what you are trying to accomplish.

.. code:: python

    for n in range(10):
        print n

References
----------
- PyLint - E0104
- PyLint - E0105
- `Stack Overflow - What does yield do? <http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python>`_
