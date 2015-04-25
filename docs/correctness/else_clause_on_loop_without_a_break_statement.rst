``else`` clause on loop without a ``break`` statement
=====================================================

The ``else`` clause of a loop is executed when the loop sequence is empty. When a loop specifies no ``break`` statement, the ``else`` clause will always execute, because the loop sequence will eventually always become empty. Sometimes this is the intended behavior, in which case you can ignore this error. But most times this is not the intended behavior, and you should therefore review the code in question.

Anti-pattern
------------

The code below demonstrates some potential unintended behavior that can result when a loop contains an ``else`` statement yet never specifies a ``break`` statement. ``contains_magic_number()`` iterates through a list of numbers and compares each number to the magic number. If the magic number is found then the function prints ``The list contains the magic number."``. If it doesn't then the function prints ``This list does NOT contain the magic number.``. When the code calls the function with a list of ``range(10)`` and a magic number of ``5``, you would expect the code to only print ``The list contains the magic number.``. However, the code also prints ``This list does NOT contain the magic number.``. This is because the ``range(10)`` list eventually becomes empty, which prompts Python to execute the ``else`` clause.

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

Best practices
--------------

Insert a ``break`` statement into the loop
..........................................

If the ``else`` clause should not always execute at the end of a loop clause, then the code should add a ``break`` statement within the loop block.

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

- PyLint - W0120
- `Python Standard Library - else Clauses on Loops <https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops>`_
