Not using ``else`` where appropriate in a loop
==============================================

Summary
-------

Use an ``else`` clause to execute code that should be executed when a loop does not get terminated by a ``break`` statement.

Description
-----------

The Python language provides a built-in ``else`` clause for ``for`` loops. If a ``for`` loop completes without being prematurely interrupted by a ``break`` or ``return`` statement, then the ``else`` clause of the loop is executed. 

Examples
----------

Not using ``else`` clause with ``for`` loop
...........................................

The module below searches a list for a magic number. If the magic number is found in the list, then the module prints ``Magic number found.``. If the magic number is not found, then the module prints ``Magic number not found.``.

The module uses a flag variable called ``found`` to keep track of whether or not the magic number was found in the list.

The logic in this module is valid; it will accomplish its task. But the Python language has built-in language constructs for handling this exact scenario and which can express the same idea much more concisely and without the need for flag variables that track the state of the module.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    l = [1, 2, 3]
    magic_number = 4
    found = False

    for n in l:
        if n == magic_number:
            found = True
            print "Magic number found."
            break

    if not found:
        print "Magic number not found."

Solutions
---------

Use ``else`` clause with ``for`` loop
.....................................

In Python, you can declare a ``else`` loop in conjunction with a ``for`` loop. If the ``for`` loop iterates to completion without being prematurely interrupted by a ``break`` or ``return`` statement, then Python executes the ``else`` clause of the loop.

In the modified module below, the ``for`` loop will iterate through all three items in the list. Because the magic number is not contained in the list, the ``if`` statement always evaluates to ``False``, and therefore the ``break`` statement is never encountered. Because Python never encounters a ``break`` statement while iterating over the loop, it executes the ``else`` clause.

The modified code below is functionally equivalent to the original code above, but this modified code is more concise than the original code and does not require any flag variables for monitoring the state of the module.

.. code:: python

    l = [1, 2, 3]
    magic_number = 4

    for n in l:
        if n == magic_number:
            print "Magic number found."
            break
    else:
        print "Magic number not found."
    
References
----------
- `Python Language Reference - else Clauses on Loops <https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops>`_
