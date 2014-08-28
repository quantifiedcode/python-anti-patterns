==============================
No exception type(s) specified
==============================

Description
===========

You handled an exception without specifying and exception type in your except-clause. This error is not critical, but is not considered `pythonic` as it might hide actual programming errors.

Example(s)
==========

The function `divide` simply devides `a` by `b`. To avoid invalid calculations (e.g., a division by zero), a `try-except` block is added. This is valid and and ensures that the function always returns a result. However, by securing your code with the try clause, you might hide acutall programming errors, e.g., that you pass a string or an object as `b`, instead of a number. By not specifiycing and exception type, you do not only hide this error but you loose also information about the error itself.

.. code:: python

    def divide(a, b):
    
        try:
          result = a / b
        except:
          result = None
          
      return result

Solution(s)
===========

Handle exceptions with Python's built in `exception types<https://docs.python.org/2/library/exceptions.html>`
-------------------------------------------------------------------------------------------------------------

.. code:: python

    def divide(a, b):
    
        result = None
    
        try:
            result = a / b
        except ZeroDivisionError:
            # Occurs, if b is zero
            print "Type error: division by 0."
        except TypeError:
            # Occurs, if b is e.g, a string
            print "Type error: division by '{0}'.".format(b)
        except Exception as e:
            # Base Exception class to handle any other error
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        else:
            # Executes only, if no exception occured
            print "No errors"
        finally:  
            # Executes if an exception occured or not
            if result is None:
                print "Setting result to 0"
                result = 0
        
        return result
            
With this pattern, you are able to handle exceptions based on their by exception-type. The first exception type that matches the actual exception is handled first. Thus, it is recommended to handle specific error types first (e.g,. ZeroDivisionError) and generic error types (e.g., Exception) towards the end of the try-except block. The `else`-clause executes only, if no exception occured. It is useful to log the success of your code. Other than the `else`-block, the `finally`-block excecutes under all circumstances — no matter if an error occured or not. It can be used to clean up your actions in the `try-except`, or, like in this example, to set `result = 0`. Both, the `else`-clause and the `finally`-clause are optional.

Implement user defined exceptions
---------------------------------

In addition to Python's standard exceptions, you can implement your own exception classes. 

.. code:: python

    class DivisorTooSmallError(StandardError):
        def __init__(self, arg):
            self.args = arg

    def divide(a, b):
    
        result = None
    
        try:
            # Raise an error if b is < 1
            if b < 1:
                raise DivisorTooSmallError
            result = a / b    
        except ZeroDivisionError:
            # Occurs, if b is zero
            print "Type error: division by 0."
        except TypeError:
            # Occurs, if b is e.g, a string
            print "Type error: division by '{0}'.".format(b)
        except DivisorToSmall:
            # Occurs, if b is below 1
            print "DivisorToSmall error: set result = 1"
            result = 1
        except Exception as e:
            # Base Exception class to handle any other error
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        else:
            # Executes only, if no exception occured
            print "No errors"
        finally:  
            # Executes if an exception occured or not
            if result is None:
                print "Setting result to 0"
                result = 0
        
        return result
    
References
==========
- `PyLint W0701<http://pylint-messages.wikidot.com/messages:w0701>`
- `Python Built-in Exceptions<https://docs.python.org/2/library/exceptions.html#exceptions.BaseException>`
- `Python Errors and Exceptions<https://docs.python.org/2/tutorial/errors.html>`
