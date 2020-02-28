No exception type(s) specified
==============================

The function `divide` simply divides `a` by `b`. To avoid invalid calculations (e.g., a division by zero), a `try-except` block is added. This is valid and ensures that the function always returns a result. However, by securing your code with the try clause, you might hide actual programming errors, e.g., that you pass a string or an object as `b`, instead of a number. By not specifying an exception type, you not only hide this error but you also lose information about the error itself.

Anti-pattern
------------

.. code:: python

    def divide(a, b):

        try:
            result = a / b
        except:
            result = None

        return result

Best practice
-------------

Handle exceptions with Python's built in `exception types <https://docs.python.org/2/library/exceptions.html>`_.

.. code:: python

    def divide(a, b):

        result = None

        try:
            result = a / b
        except ZeroDivisionError:
            print("Type error: division by 0.")
        except TypeError:
            # E.g., if b is a string
            print("Type error: division by '{0}'.".format(b))
        except Exception as e:
            # handle any other exception
            print("Error '{0}' occured. Arguments {1}.".format(e.message, e.args))
        else:
            # Excecutes if no exception occured
            print("No errors")
        finally:
            # Executes always
            if result is None:
                result = 0

        return result

With this pattern, you are able to handle exceptions based on their actual exception-type. The first exception type that matches the current error is handled first. Thus, it is recommended to handle specific exception types first (e.g., ZeroDivisionError) and generic error types (e.g., Exception) towards the end of the try-except block.

**Cleanup actions (optional)**: The `else`-clause executes only, if no exception occurred. It is useful to log the success of your code. The `finally`-block executes under all circumstances — no matter if an error occured or not. It is useful to clean up the `try-except` block.

Implement user defined exceptions
---------------------------------

In addition to Python's standard exceptions, you can implement your own exception classes.

.. code:: python

    class DivisorTooSmallError(StandardError):
        def __init__(self, arg):
            self.args = arg


    def divide(a, b):
        if b < 1:
            raise DivisorTooSmallError
        return a / b


    try:
        divide(10, 0)
    except DivisorTooSmallError:
        print("Unable to divide these numbers!")

References
----------

- PyLint W0702, bare-except
- `Python Built-in Exceptions<https://docs.python.org/2/library/exceptions.html#exceptions.BaseException>`
- `Python Errors and Exceptions<https://docs.python.org/2/tutorial/errors.html>`


