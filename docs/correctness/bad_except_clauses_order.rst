Bad except clauses order
========================

Summary
-------

Raised when a base class exception clause is placed before its sub class exception clauses. Whenever an exception is raised which matches the sub class, the base class exception clause will always be called. The exception clause doesn't need to be an exact match of the raised exception; so long as the raised exception is a sub class of the exception defined in the exception clause then that exception clause will execute. This defeats the purpose of catching exceptions, which is to pinpoint the exact reason why an exception occurred. Place the sub class exception clauses before the base class exception clause.

Description
-----------

When an exception occurs, Python will search for the first exception clause which matches the exception type that occurred. It doesn't need to be an exact match. If the exception clause represents a base class of the raised exception, then Python considers that exception clause to be a match. E.g. if a ``ZeroDivisionError`` exception is raised and the first exception clause is ``Exception``, then the ``Exception`` clause will execute because ``ZeroDivisionError`` is a sub class of ``Exception``. Therefore, more specific exception clauses of sub classes should always be placed before the exception clauses of their base classes to ensure that exception handling is as specific and as helpful as possible.

Examples
----------

Sub class exception clause placed after its ancestor's clause
.............................................................

The module below performs a division operation that results in a ``ZeroDivisionError``. The module contains an except clause for this type of error, which would be really useful because it pinpoints the exact cause of the problem. However, the ``ZeroDivisionError`` exception clause is unreachable because there is a ``Exception`` exception clause placed before it. When Python experiences an exception, it will linearly test each exception clause and execute the first clause that matches the raised exception. The match does not need to be identical. So long as the raised exception is a sub class of the exception listed in the exception clause, then Python will execute that clause and will skip all other clauses. This defeats the purpose of exception clauses, which is to identify and handle exceptions with as much precision as possible.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    try: 
        5 / 0
    except Exception as e:
        print "Exception"
    except ZeroDivisionError as e:  # unreachable code!
        print "ZeroDivisionError"

Solutions
---------

Move sub class exception clause before its ancestor's clause
............................................................

The modified module below places the ``ZeroDivisionError`` exception clause in front of the ``Exception`` exception clause. Now when the exception is triggered the ``ZeroDivisionError`` exception clause will execute, which is much more optimal because it is more specific.

.. code:: python

    try: 
        5 / 0
    except ZeroDivisionError as e:
        print "ZeroDivisionError"
    except Exception as e:
        print "Exception"

References
----------
