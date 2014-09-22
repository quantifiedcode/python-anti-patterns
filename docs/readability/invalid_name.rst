Invalid name
============

Summary
-------

The name of an object does not match the naming convention for its type (variable, constant, etc.). This error is just a stylistic warning. The code will probably execute. But you can improve the readability of the code by renaming the object to match the naming conventions for that type of object.

Description
-----------

The table below describes the naming conventions for various types of objects. 

.. csv-table::
    :header: "Type", "Regular Expression Pattern"

    "Argument", "[a-z_][a-z0-9_]{2,30}$"
    "Attribute", "[a-z_][a-z0-9_]{2,30}$"
    "Class", "[A-Z_][a-zA-Z0-9]+$"
    "Constant", "(([A-Z_][A-Z0-9_]*)|(__.*__))$"
    "Function", "[a-z_][a-z0-9_]{2,30}$"
    "Method", "[a-z_][a-z0-9_]{2,30}$"
    "Module", "(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$"
    "Variable", "[a-z_][a-z0-9_]{2,30}$"
    "Variable, Inline", "[A-Za-z_][A-Za-z0-9_]*$"

Examples
----------

Function name does not follow naming convention
...............................................

The function named ``Hello`` below does not follow the standard naming convention for functions. As indicated in the table above in the "Description" section of this article, functions are supposed to begin with a lower case letter. The problem with ``Hello`` is that it begins with an upper case letter. The program executes, but other programmers may find the code hard to read, because classes are usually the only objects that begin with upper case letters.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def Hello():  # does not follow naming convention for functions
        print "Hello, World!"

    Hello()  # hard to read, looks like a class

Solutions
---------

Fix the function name to follow naming convention
.................................................

In the modified module below, the function name has been modified to follow the typical naming convention for functions. The function ``hello`` now begins with a lower case letter. Note that the module also needs to replace every invocation of the function, not just the function definition.

.. code:: python

    def hello():  # replace H with h
        print "Hello, World!"

    hello()  # easier to read, looks like a function

References
----------
- `PyLint - C0103 <http://pylint-messages.wikidot.com/messages:c0103>`_
