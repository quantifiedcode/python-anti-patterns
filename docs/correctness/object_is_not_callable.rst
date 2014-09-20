Object is not callable
======================

Summary
-------

The specified object is not something that can be called. This typically happens when two objects, such as a module and a function, share the same name and the wrong object is called. The statement needs to be fixed or else Python will raise a ``TypeError`` and the module will not execute successfully.

Description
-----------

The ``object is not callable`` error is usually encountered when two objects, such as a class and a method, or a module and a function, have the same name. This can be solved by fully qualifying the function when calling it, or using more specific ``import`` statements.

Examples
----------

Ambiguous scope leads to calling the wrong object
.................................................

The module attempts to import the ``random`` module and then call the ``random`` function from that module. Python raises a ``TypeError`` and the module does not execute because, in this scope, ``random`` refers to the module ``random``, not the function.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import random

    print random()  # TypeError: random refers to the module here

Solutions
---------

Fully qualify the function
..........................

The modified module below suppresses the ``object is not callable`` error by fully qualifying the ``random`` function when calling it.

.. code:: python

    import random

    print random.random()  # fully qualified function eliminates ambiguity

Use more specific import statements
...................................

Another way to fix the ``object is not callable`` error is to use more specific import statements. In the modified module below, the module uses the import statement ``from random import random`` to specifically import the ``random`` function from the ``random`` module.

.. code:: python

    from random import random

    print random()

References
----------
- `Stack Overflow - What is a callable? <http://stackoverflow.com/questions/111234/what-is-a-callable-in-python>`_
