Not using named tuples when returning more than one value from a function
=========================================================================

Summary
-------

Use named tuples when returning more than one value from a function. This makes code easier to read and makes the data easier to access, as each value can be accessed via a name in addition to an index.

Description
-----------

Named tuples can be used anywhere where normal tuples are acceptable, but their values can be accessed through their name in addition to their index, which makes code more verbose and easier to read.

Examples
----------

Using normal tuple to return multiple values
............................................

The module below returns a first name, middle name, and last name using a normal, unnamed tuple. After calling the tuple, each value can only be returned via an index. This code is difficult to use: the caller of the function has to know that the first element is the first name, the second is the middle name, and the third is the last name.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def get_name():
        return "Richard", "Xavier", "Jones"

    name = get_name()

    print name[0], name[1], name[2]  # ('Richard', 'Xavier', 'Jones')  # hard to read

Solutions
---------

Use named tuples to return multiple values
..........................................

The modified module below uses named tuples to return multiple values. This code is easier to use and easier to read, as now the caller can access each piece of data via a straightforward name (like ``name.first``).

.. code:: python

    from collections import namedtuple

    def get_name():
        name = namedtuple("name", ["first", "middle", "last"])
        return name("Richard", "Xavier", "Jones")

    name = get_name()

    print name.first, name.middle, name.last  # much easier to read

References
----------
- `Python Standard Libary - collections.namedtuple <https://docs.python.org/2/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields>`_
