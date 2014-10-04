Using ``key in list`` to check if key is contained in list
==========================================================

Summary
-------

Using ``key in list`` to check if an item is contained in a list is not an error but it is inefficient, since the list search will take O(n). If possible, use a set or dictionary instead, which enables Python to attempt to directly access the item without iterations.

Description
-----------

Using ``key in list`` to iterate through a list can potentially take ``n`` iterations to complete, where ``n`` is the number of items in the list. If possible, you should change the list to a set or dictionary instead, becase Python can search for items in a set or dictionary by attempting to directly accessing them without using any iterations, which is much more efficient.

Examples
----------

Using ``key in list`` to check if a key exists
..............................................

The module below defines a list ``l`` and then calls ``if 3 in l`` to check if the number 3 exists in the list. This is inefficient. Behind the scenes, Python iterates through the list until it finds the number or reaches the end of the list.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    l = [1, 2, 3, 4]
    
    if 3 in l:
        print "The number 3 is in the list."
    else:
        print "The number 3 is NOT in the list."

Solutions
---------

Use a set or dictionary instead of a list
.........................................

In the modified module below, the list has been changed to a set. This is much more efficient behind the scenes, as Python can attempt to directly access the target number in the set, rather than iterate through every item in the list and compare every item to the target number.

.. code:: python

    s = set(1, 2, 3, 4)
    
    if 3 in s:
        print "The number 3 is in the list."
    else:
        print "The number 3 is NOT in the list."
    
References
----------
