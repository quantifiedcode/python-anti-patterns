The loop may never terminate
============================

Summary
-------

The given loop does not modify anything that impacts the loop condition and does not call ``break``, ``return``, or ``yield`` explicitly. Therefore, this loop will probably never terminate.

Description
-----------

Possible infinite loops should be treated as fatal mistakes, because once the module enters an infinite loop it will never be able to exit it.

Examples
----------

Loop does not modify anything that impacts the loop condition
.............................................................

The module below creates a ``while`` loop that is supposed to print out the numbers 0 through 9. However, the author of the module forgot to increment the variable used in the loop condition, so this loop will execute forever.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    i = 0

    while i < 10:
        print i
        # infinite loop! forgot to increment i

Solutions
---------

Modify the variable that impacts the loop condition
...................................................

In the modified module below, the loop finishes as expected, because now the variable ``i`` is incremented by 1 in every iteration of the loop.

.. code:: python

    i = 0
  
    while i < 10:
        print i
        i += 1  # no more infinite loop
    
References
----------
