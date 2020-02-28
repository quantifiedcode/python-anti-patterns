Returning more than one variable type from function call
========================================================

If a function that is supposed to return a given type (e.g. list, tuple, dict) suddenly returns
something else (e.g. ``None``) the caller of that function will always need to check the type of the
return value before proceeding. This makes for confusing and complex code. If the function is unable
to produce the supposed return value it is better to raise an exception that can be caught by the caller instead.

Anti-pattern
------------

In the code below, the function ``get_secret_code()`` returns a secret code when the code calling the function provides the correct password. If the password is incorrect, the function returns ``None``. This leads to hard-to-maintain code, because the caller will have to check the type of the return value before proceeding.

.. code:: python

    def get_secret_code(password):
        if password != "bicycle":
            return None
        else:
            return "42"

    secret_code = get_secret_code("unicycle")

    if secret_code is None:
        print("Wrong password.")
    else:
        print(f"The secret code is {secret_code}")



Best practice
-------------

Raise an exception when an error is encountered or a precondition is unsatisfied
........................................................................

When invalid data is provided to a function, a precondition to a function is not satisfied, or an error occurs during the execution of a function, the function should not return any data. Instead, the function should raise an exception. In the modified version of ``get_secret_code()`` shown below, ``ValueError`` is raised when an incorrect value is given for the ``password`` argument.

.. code:: python

    def get_secret_code(password):
        if password != "bicycle":
            raise ValueError
        else:
            return "42"

    try:
        secret_code = get_secret_code("unicycle")
        print(f"The secret code is {secret_code}")
    except ValueError:
        print("Wrong password.")


