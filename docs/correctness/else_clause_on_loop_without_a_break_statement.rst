``else`` clause on loop without a ``break`` statement
=====================================================

Summary
-------

A loop contains an ``else`` clause yet specifies no ``break`` statement. The ``else`` clause executes when the loop sequence is empty. Because the loop has no break statement the ``else`` clause will always execute as the last iteration of the loop sequence. Check the code to verify that this is the intended behavior.

Description
-----------

The ``else`` clause of a loop is executed when the loop sequence is empty. When a loop specifies no ``break`` statement, the ``else`` clause will always execute, because the loop sequence will eventually always become empty. Sometimes this is the intended behavior, in which case you can ignore this error. But most times this is not the intended behavior, and you should therefore review the code in question.

Examples
----------

Loop contains ``else`` clause yet specifies no ``break`` statements
...................................................................

The code below demonstrates some potential unintended behavior that can result when a loop contains an ``else`` statement yet never specifies a ``break`` statement. ``contains_magic_number()`` iterates through a list of numbers and compares each number to the magic number. If the magic number is found then the function prints ``The list contains the magic number."``. If it doesn't then the function prints ``This list does NOT contain the magic number.``. When the module calls the function with a list of ``range(10)`` and a magic number of ``5``, you would expect the module to only print ``The list contains the magic number.``. However, the module also prints ``This list does NOT contain the magic number.``. This is because when the ``range(10)`` list eventually becomes empty, which prompts Python to execute the ``else`` clause.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def contains_magic_number(list, magic_number):
        for i in list:
            if i == magic_number:
                print "This list contains the magic number."
        else:
            print "This list does NOT contain the magic number."

    contains_magic_number(range(10), 5)
    # This list contains the magic number.
    # This list does NOT contain the magic number.

Solutions
---------

Insert a ``break`` statement into the loop
..........................................

If the ``else`` clause should not always execute at the end of a loop clause, then the module should add a ``break`` statement within the loop block.

.. code:: python

    def contains_magic_number(list, magic_number):
        for i in list:
            if i == magic_number:
                print "This list contains the magic number."
                break  # added break statement here
        else:
            print "This list does NOT contain the magic number."

    contains_magic_number(range(10), 5)
    # This list contains the magic number.
    
References
----------
- `Python Standard Library - else Clauses on Loops <https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops>`_
