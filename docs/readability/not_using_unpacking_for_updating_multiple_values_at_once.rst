Not using unpacking for updating multiple values at once
========================================================

Summary
-------

For simple updates to multiple variables, use unpacking to update the values rather than using assignments to update each value individually.

Description
-----------

In general, the Python programming community prefers concise code over verbose code. Using unpacking to update the values of multiple variables simultaneously is more concise than using assignments to update each variable individually. 

Examples
----------

Using assignments to individually update the values of variables
................................................................

The module below updates the values of the two variables ``x`` and ``y`` using assignments that are on separate lines of code.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    x = 1
    y = 2
    z = 0
    
    # The method below is not the preferred way to update multiple values
    x = y + 2  # 4
    y = x - 3  # 1
    z = x + y  # 5

Solutions
---------

Use unpacking to update multiple values simultaneously
......................................................

The modified module below is functionally equivalent to the original module above, but this module is more concise. 

.. code:: python

    x = 1
    y = 2
    z = 0

    x, y, z = y + 2, x - 3, x + y  # more concise
    
References
----------
