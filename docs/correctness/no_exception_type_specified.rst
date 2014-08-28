===============
No exception type(s) specificied
===============

Description
===========

You handled an exception without a specific error type. This error is not critical, but is not considered `pythonic`.

Example(s)
==========

The function `divide` simply devides `a` by `b`. To avoid invalid calculations (e.g., a division by zero), a `try-except` block is added. This is valid and and ensures that the function always returns a result. However, it is not considered `pythonic` as it might hide actual programming errors.

.. code:: python

    def divide(a, b):
    
        try:
          result = a / b
        except:
          result = None
          
      return result

Solution(s)
===========

# Handle exceptions with Python's built in `exception types<https://docs.python.org/2/library/exceptions.html>`
    
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
                print "Set result to 0"
                result = 0
        
        return result
            
    With this pattern, you are able to handle errors specifically by error-type. The first error class that actually mathches the actual error is executed first. Thus, it is recommended to start handling specific error types first (e.g,. ZeroDivisionError) and generic error types towards the end of the try-except block. The `else`-clause is less known but very useful. It executes only, if no exception occured. Other than the `else`-block, the `finally`-block excecutes under all circumstances, not matter if an error occured or not. It can be used to clean up your actions in the `try-except`, or, like in this example, to set `result = 0`. Both, the `else`-clause and the `finally`-clause are optional.

- Create user defined exceptions


    .. code:: python

        def func()
            return
    
References
==========
- `PyLint W0701 <http://pylint-messages.wikidot.com/messages:w0701>`_
