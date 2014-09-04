Dangerous default value %s as argument
======================================

Summary
-------

When a mutable list or dictionary is passed as a default argument to a method or function, Python creates a single persistent object and then uses that object for every subsequent call in which the argument is left empty. This can cause problems if the program was expecting the function to return a new list or dictionary after every call.

Description
-----------

Passing mutable lists or dictionaries as default arguments can have unforeseen consequences. Usually when a programmer uses a list or dictionary as the default argument to a function, the programmer wants the program to create a new list or dictionary every time that the function is called. However, this is not what Python does. The first time that the function is called, Python creates a persistent object for the list or dictionary. Every subsequent time the function is called, Python uses that same persistent object that was created from the first call to the function.

Examples
----------

A mutable list or dictionary is supplied as the default argument
................................................................

.. code:: python



Solutions
---------

Use a sentinel value to denote an empty list or dictionary
..........................................................

.. code:: python



References
----------
- `PyLint - W0102 <http://pylint-messages.wikidot.com/messages:w0102>`_
- `Stack Overflow - Hidden Features of Python <http://stackoverflow.com/questions/101268/hidden-features-of-python#113198>`_
