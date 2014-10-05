Putting type notation in a variable name 
========================================

Summary
-------

Putting type notation in a variable name is potentially misleading, because there is nothing in the Python language which can actually enforce that the variable type actually matches the type notation described in the name. Consider removing the type notation.

Description
-----------

Python is a duck-typed language. Just because a variable is described as an integer, does not mean that it actually is an integer. This can be very dangerous for any programmer who acts on the variable assuming that it is an integer. Note that the practice of including type notation in variable names is also called Hungarian Notation.

Examples
----------

Using type notation in variable names
.....................................

The module below demonstrates the dangers of variables whose names include type notation. Just because a variable is called ``n_int`` does not mean that the variable actually contains an integer for its value.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    n_int = "Hello, World!"

    4 / n_int  # mistakenly assuming that n_int is a number


Solutions
---------

Remove type notation
....................

Although the modifed module below does not fix the underlying problem of attempting to divide a number by a string, the code is generally less misleading, because there is no misleading description in the variable name ``n`` that ``n`` is a number.

.. code:: python

    n = "Hello, World!"

    4 / n  # still a problem, but less likely to occur now
    
References
----------
`Stack Overflow - Hungarian Notation <http://stackoverflow.com/questions/8791533/does-it-make-sense-to-use-hungarian-notation-prefixes-in-interpreted-languages>`_
