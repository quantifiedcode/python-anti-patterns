Returning more than one variable type from function call
========================================================

Summary
-------

A function call should return only one type of variable. If an error occurs or some precondition is not met, the function should not return ``None`` or any other value. It should raise an exception.

Description
-----------

If a function that is supposed to return a given type (e.g. list, tuple, dict) suddenly returns
something else (e.g. ``None``) the caller of that function will always need to check the type of the
return value before proceeding. This makes for confusing and complex code. If the function is unable
to produce the supposed return value it is better to raise an exception that can be caught by the caller instead.

Example: If a function is supposed to return a list, do not return None if an 
error occurs or some condition is unmet. Instead, raise an exception.


Examples
----------

Function returns ``None`` upon unsatisfied precondition
.......................................................

In the module below, the function ``get_secret_code()`` returns a secret code when the module calling the function provides the correct password. If the password is incorrect, the function returns ``None``. This leads to hard-to-maintain code, because the caller will have check the type of the return value before proceeding.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def get_secret_code(password):
        if password != "bicycle":
            return None
        else:
            return "42"

    secret_code = get_secret_code("unicycle")

    if secret_code == None:
        print "Wrong password."
    else:
        print "The secret code is %s".format(secret_code)
        

Solutions
---------

Raise exception when error is encountered or precondition is unsatisfied
........................................................................

When a calling module provides invalid data to a function, or a precondition to the function is not satisfied, or an error occurs during the execution of the function, the function should not return any data. The function should raise an exception. In the modified version of the ``get_secret_code()`` function below, the function raises a ``ValueError`` when a calling module does not provide the correct value for the ``password`` argument.

.. code:: python

    def get_secret_code(password):
        if password != "bicycle":
            raise ValueError
        else:
            return "42"

    try:
        secret_code = get_secret_code("unicycle")
        print "The secret code is %s".format(secret_code)
    except ve as ValueError:
        print "Wrong password."

References
----------
