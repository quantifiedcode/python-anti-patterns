Undefined name
==============

Summary
-------

Raised when a module attempts to use a name that has not been defined. The statement referencing the undefined name must be removed, or the name must be implemented, or else Python will not be able to execute the program.

Description
-----------

When a module attempts to use a name which has not been defined, Python will immediately stop executing and return a ``NameError``. 

Examples
----------

Object not implemented
..................................

The module ``names`` below attempts to use a variable called ``middle`` which has not been defined. When Python encounters this code it will immediately stop executing and raise a ``NameError`` error.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """names.py"""
    first = "Grace"
    last = "Kelly"

    print first
    print middle  # undefined
    print last

Solutions
---------

Remove the statement referencing the undefined name 
...................................................

Removing the statement that references the undefined name will suppress the ``NameError`` error. In the ``names`` module below the offending statement ``print middle`` has been commented out.

.. code:: python

    """names.py"""
    first = "Grace"
    last = "Kelly"

    print first
    # print middle
    print last
   

Implement the name
..................

Implementing the undefined name as some type of object (variable, function, etc.) also suppresses the ``NameError`` error. In the ``names`` module below the previously undefined name ``middle`` has been implemented as a variable.

.. code:: python

    """names.py"""
    first = "Grace"
    middle = "Patricia"
    last = "Kelly"

    print first
    print middle  # ok now, because "middle" is implemented
    print last
 
References
----------
- Pyflakes - F821
