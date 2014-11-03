Unused variable
===============

Summary
-------

A variable has been defined but is not being used. Review the module in question and check if the module is missing any implemenatation. To improve code readability and performance, delete the variable in question if it is no longer needed.

Description
-----------

This error is often triggered when someone refactors a module but misses a reference to a variable that is no longer needed. Other times it indicates that someone has forgotten to implement a section of the module's logic. Therefore, treat this error as a warning and review the code in question.

Examples
----------

Unused variable in function
...........................

For no apparent reason, the module below defines a variable named ``banana`` which is not used anywhere else in the function. This ``banana`` variable causes the ``unused variable`` error.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_string(string):
        banana = "banana"  # causes "unused variable`` error
        print string

    print_string("Hello, World!")

Solutions
---------

Remove the unused variable
..........................

Upon reviewing the module, the author decides that the ``banana`` variable serves no purpose, so he deletes it. The code is now easier to read, more efficient, and the ``unused variable`` error is suppressed.

.. code:: python

    def print_string(string):
        print string

    print_string("Hello, World!")    

Use the variable
................

After receiving the ``unused variable`` error the author reviews the section of code in question to check if any logic is missing. Upon reviewing the module he realizes that he has forgotten a critical piece of logic, which is to let everybody know what his favorite fruit is.

.. code:: python

    def print_string(string):
        var banana = "banana"
        print "My favorite fruit is {:s}.".format(banana)
        print string

    print_string("Hello, World!")  
    
References
----------
- PyLint - W0612
