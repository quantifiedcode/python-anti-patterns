Using possibly undefined loop variable
======================================

Summary
-------

A loop variable (i.e. a variable defined in a for or while loop) is being used outside of the scope of the loop. This can potentially result in unintended or undefined behavior. Either move the statements outside the scope of the loop into its scope, or define the variable outside the loop scope.

Description
-----------

This error is often encountered when someone does not properly indent a statement and the statement is unintentionally executed outside the scope of the loop. Use this error as a warning to review the code in question and make sure there are no indentation errors.

Examples
----------

Loop statement not indented properly
....................................

In the module below the author wants to add the numbers 1 through 9 to a list. However, the statement that adds the numbers to the list (``s.append(n)``) is not indented properly, so it executes at the global scope, not the loop scope as the author intended. When printing out ``s`` the author expects it to contain a list of numbers 1 through 9, but it actually only contains the number 9.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    s = []
    for n in range(10):
        print n
    s.append(n)  # only executes once. appends last value assigned to n, which is 9
    print s  # [9]

Solutions
---------

Fix statement indentation to change scope 
.........................................

The modified module below indents the statement ``s.append(n)`` to clarify that this statement should be executed within the scope of the loop.

.. code:: python

    s = []
    for n in range(10):
        print n
        s.append(n)  # loop scope now, executes 10 times
    print s  # [9]

References
----------
- PyLint - W0631
