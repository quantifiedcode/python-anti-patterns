Import module from line n shadowed by loop variable
===================================================

Summary
-------

A loop has defined a variable with the same name as an imported module. This can cause bugs in a module because it overrides the meaning of the module name. Attempting to access module members after the module name has been redefined can result in runtime errors or unintended behavior. The variable name should be renamed to something other than a module name.

Description
-----------

Using the name of an imported module as the name for a loop variable overrides the meaning of the name. Outside of the loop construct, the name refers to the module. But inside of the loop construct, the name refers to the variable. So any attempt to access module members inside of the loop will cause errors or unintended behavior.

Examples
----------

Loop defines variable with same name as imported module
.......................................................

The module below imports the ``os`` Python Standard Library module, which is used for performing miscellaneous tasks related to the current operating system. When ``os.name`` is called, ``os`` still refers to the ``os`` module, so this works fine. But when the for loop creates a variable called ``os`` this overrides the meaning of ``os``. ``os`` now refers to a ``str`` variable. So only members from the ``str`` class are valid on ``os`` now. Any attempt to reference a member from the ``os`` module creates runtime errors. In other words, when the module attempts to reference ``os.name`` in the for loop, it is actually calling ``str.name``. Because the ``str`` data type does not have any member called ``name`` Python raises an error.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import os

    print os  # <module 'os' from '/usr/lib/python2.7/os.pyc'> or something similar
    print os.name  # prints operating system name, as defined in os module

    for os in ["Windows", "Mac OS X", "Linux"]:  # string var overshadows string module
        print os.name  # AttributeError: str has no attribute name 
        print os  # never executes because of error above

Solutions
---------

Give loop variables unique names
................................

A for loop variable should never use the name of an imported module. In the modified module below, the for loop variable name has been changed from ``os`` to ``os_name``, which eliminates the ambiguity that caused problems in the original module.

.. code:: python

    import os

    print os  # <module 'os' from '/usr/lib/python2.7/os.pyc'> or something similar
    print os.name  # prints operating system name, as defined in os module

    for os_name in ["Windows", "Mac OS X", "Linux"]:  # variable name is unique now
        print os.name  # prints operating system name, as defined in os module
        print os_name  # prints "Windows", "Mac OS X", "Linux"
    
References
----------
- Pyflakes - F402
