Local variable name is assigned to but never used
=================================================

Summary
-------

A local variable in a function is not being used. This is usually caused when someone starts implementing a function but never finishes it, or someone has refactored a function but forgot to remove old parts of the function that are no longer used. Therefore you should go back and review the function to make sure it has no problems.

Description
-----------

When you encounter this error, you should go back and check the function in question, because there is probably a problem with it. If someone forgot to implement part of the function, go back to the function and finish its implementation. If someone refactored the function but forgot to clean it up, remove all unused variables so that the function is easier to read and does not waste memory.

Examples
----------

Local variable is assigned in function but never used
.....................................................

In the ``area`` function below the ``a`` variable is assigned to the product of ``width * height`` but the variable is never used. The programmer who wrote the function has left a ``todo`` comment reminding himself that he needs to implement logging later on.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def area(width, height):
        a = width * height
        # todo: implement logging using variable a
        return width * height

Solutions
---------

Remove the variable if it is unnecessary
........................................

Remove the variable if you have no plans on using it. This improves the readability and performance of the function.

.. code:: python

    def area(width, height):
        return width * height


Finish implementing the function
................................

If the variable is a reminder of some part of the function that still needs to be implemented, then go back and finish implementing the function.

.. code:: python

    import logging

    def area(width, height):
        a = width * height
        logging.info(a)
        return a

References
----------
- Pyflakes - F841
