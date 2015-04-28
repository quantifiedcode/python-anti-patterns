Not using unpacking for updating multiple values at once
========================================================

In general, the Python programming community prefers concise code over verbose code. Using unpacking to update the values of multiple variables simultaneously is more concise than using assignments to update each variable individually.

Anti-pattern
------------

The function below implements the classical Euclid algorithm for greatest common divisor.
The updates of the variables ``a`` and ``b`` are made using variable ``temp`` and three lines of code.

.. code:: python

    def gcd(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

Best practice
-------------

Use unpacking to update multiple values simultaneously
......................................................

The modified code below is functionally equivalent to the original code above, but this code is more concise.

.. code:: python

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


Gotchas
-------

The unpacking can be sometimes quite misleading. Figure out what is the outcome of the code below.

.. code:: python

    b = "1984"
    a = b, c = "AB"
    print a, b, c
