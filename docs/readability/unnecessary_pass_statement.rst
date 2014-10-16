Unnecessary pass statement
==========================

Summary
-------

A function or control block contains an unnecessary ``pass`` statement. A ``pass`` statement is unnecessary when a function or control block is non-empty. Unnecessary pass statements are harmless, but they reduce code readability. 

Description
-----------

The ``pass`` statement should only be used to signify that a function or control block requires no action, or to signify a placeholder for a block of code that will be implemented later. When a function or control block only contains a ``pass`` statement, then you can infer that the ``pass`` statement is a necessary indicator that no further action is required or that this block of code will be implemented in the future. If the function or control block contains other statements, then the ``pass`` statement is unnecessary. Therefore, whenever a ``pass`` statement is not the *only* statement in a function or control block, then it is considered unnecessary and should be removed.

Examples
----------

``pass`` statement in implemented function
..........................................

In the ``hello_world`` function below the ``pass`` statement is unnecessary because there is another statement implemented in the function (``print "Hello, World!"``). A pass statement is unnecessary whenever it is not the *only* statement in a function or control block. 

.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def hello_world():
        print "Hello, World!"
        pass # unnecessary

Solutions
---------

Remove the ``pass`` statement
.............................

Removing the ``pass`` statement suppresses the ``Unnecessary pass statement`` error.

.. code:: python

    def hello_world():
        print "Hello, World!"

References
----------
- `PyLint - W0107 <http://pylint-messages.wikidot.com/messages:w0107>`_
- `Python Language Reference <https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement>`_
