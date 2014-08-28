===============
No exception type(s) specificied
===============

Description
===========

You handled an exception without a specific error type. This error is not critical, but is not considered `pythonic`.

Example(s)
==========

The following function devides `a` by `b`. To avoid invalid calculations (e.g., a division by zero), a `try-except` block is added. 


.. code:: python

    def func(a, b):
        try:
          result = a / b
        except:
          result = 0
      return result

Solution(s)
===========

- Handle exceptions with Python's built in `exception types<https://docs.python.org/2/library/exceptions.html>`
    
    .. code:: python

        def func(a, b):
            
            try:
                result = a / b
            
            except ZeroDivisionError:
                # Occurs, if b is zero
                print "Type error: division by 0"
            
            except TypeError:
                # Occurs, if b is e.g, a string
                print "Type error: division by '{0}'".format(b)
                
            except Exception as e:
                # Base Exception class to handle any other error
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)

            else:
                # Executes after an exception, not matter which type
                result = None
            
            finally:  
                # Executes always, even without exception
                print "Done!"
            
            return result
            
    With this pattern, you are able to handle errors specifically by error-type. The `else`-clause executes, not matter which error occured. If, like in this example, we want to return `None`, not matter which exception occured, we need to set `result = None` only once. Other than the `else`-block, the `finally`-block excecutes under all circumstances, not matter if an error occured or not. It can be used to clean up your actions in the `try-except`.

- Create user defined exceptions


    .. code:: python

        def func()
            return
    
References
==========
- `PyLint W0701 <http://pylint-messages.wikidot.com/messages:w0701>`_
