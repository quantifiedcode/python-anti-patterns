Putting type information in a variable name
===========================================

Python is a duck-typed language. Just because a variable is described as an integer does not mean that it actually is an integer. This can be very dangerous for any programmer who acts on the variable assuming that it is an integer. Note that the practice of including type notation in variable names is also called Hungarian Notation.

Anti-pattern
------------

The code below demonstrates the dangers of variables whose names include type notation. Just because a variable is called ``n_int`` does not mean that the variable is actually an integer.

.. code:: python

    n_int = "Hello, World!"

    4 / n_int  # mistakenly assuming that n_int is a number


Best practice
-------------

Remove type notation
....................

Although the modifed code below does not fix the underlying problem of attempting to divide a number by a string, the code is generally less misleading, because there is no misleading description in the variable name ``n`` that ``n`` is a number.

.. code:: python

    n = "Hello, World!"

    4 / n  # still a problem, but less misleading now

References
----------

- `Stack Overflow - Hungarian Notation <http://stackoverflow.com/questions/8791533/does-it-make-sense-to-use-hungarian-notation-prefixes-in-interpreted-languages>`_
