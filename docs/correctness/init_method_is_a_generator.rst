``__init__`` method is a generator
==================================

Summary
-------

The ``__init__`` method of a class contains a ``yield`` statement, which makes it a generator. ``__init__`` is only used for initializing the values of the class. It cannot yield values. Remove the generator functionality or else the module will cause runtime errors.

Description
-----------

When Python encounters a ``yield`` statement in the ``__init__`` method of class, it raises a ``TypeError`` and halts execution of the module. ``__init__`` should only be used to initialize members of the class object, not yield any values. The generator functionality should be moved to a different method and the ``__init__`` method should only return ``None``.

Examples
----------

``__init__`` method contains ``yield`` statement
................................................

The author of the class below wants to generate a set of 10 random numbers. For maximum convenience he is attempting to generate the random numbers directly in the ``__init__`` method of the class. However, Python does not allow this. Attempting to yield any values within an ``__init__`` method causes a ``TypeError`` at runtime.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import random

    class RandomNumbers:
        def __init__(self):
            for n in range(10):
                yield random.random()  # TypeError: __init__ is a generator

    random_number_list = RandomNumbers()

Solutions
---------

Remove the yield statement from ``__init__``
............................................

To suppress the ``__init__ method is a generator`` error the author modifies the class to no longer yield any values directly from the ``__init__`` method. Rather, the class generates the random numbers and then stores them in a list. 

.. code:: python

    import random

    class RandomNumbers:
        def __init__(self):
            self.random_number_list = []
            for n in range(10):
                self.random_number_list.append(random.random())

    r = RandomNumbers()
    print r.random_number_list

References
----------
- PyLint - E0100
- `Stack Overflow - What does the yield keyword do in Python? <http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python>`_
