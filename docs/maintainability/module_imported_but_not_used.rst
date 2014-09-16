Module imported but not used
============================

Summary
-------

An imported module is not being used. The ``module imported but not used`` error typically occurs when someone forgets to implement a section of code, removes an old section of code (which used to use the module), or misspells the module name or any of the public objects available from the module. Therefore when you encounter the ``module imported but not used`` error you should review the module under question for any errors.


Description
-----------

This error typically means that there is an error in the module implementation, so you should review the module under question. There are typically three ways to solve the ``module imported but not used`` error. You can remove the module if it is not needed, check that all sections of the module have been fully implemented (and implement them if not), and check for misspellings of the module name, or any of the public objects available from the module (and fix the mispellings).

Examples
----------

Module imported but not used
............................

The module below prints out the current UNIX Epoch time. The module imports the ``math`` module but does not use any public objects from the ``math`` module.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import math
    import time

    print "Current Unix EPOCH time:", time.time()

Solutions
---------

Remove the module
.................

Upon reviewing the module, the owner of the module decided that the ``math`` module was not needed, so he removed the ``import math`` statement. Because the module is no longer imported the ``module imported but not used`` error is no longer valid.

.. code:: python

    # removed import math from here
    import time

    print "Current UNIX Epoch time:", math.floor(time.time())

Use the module
..............

In the modified version of the module below, the module now uses ``math.floor`` to round calculated Epoch time value down to an integer. Because the ``math`` module is now being used the ``module imported but not used`` error is no longer raised.

.. code:: python

    import math
    import time

    print "Current UNIX Epoch time:", math.floor(time.time())  # now uses a function from the math module

    
References
----------
