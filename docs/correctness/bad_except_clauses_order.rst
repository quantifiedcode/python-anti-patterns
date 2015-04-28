Bad except clauses order
========================

When an exception occurs, Python will search for the first exception clause which matches the exception type that occurred. It doesn't need to be an exact match. If the exception clause represents a base class of the raised exception, then Python considers that exception clause to be a match. E.g. if a ``ZeroDivisionError`` exception is raised and the first exception clause is ``Exception``, then the ``Exception`` clause will execute because ``ZeroDivisionError`` is a sub class of ``Exception``. Therefore, more specific exception clauses of sub classes should always be placed before the exception clauses of their base classes to ensure that exception handling is as specific and as helpful as possible.

Anti-pattern
------------

The code below performs a division operation that results in a ``ZeroDivisionError``. The code contains an except clause for this type of error, which would be really useful because it pinpoints the exact cause of the problem. However, the ``ZeroDivisionError`` exception clause is unreachable because there is a ``Exception`` exception clause placed before it. When Python experiences an exception, it will linearly test each exception clause and execute the first clause that matches the raised exception. The match does not need to be identical. So long as the raised exception is a sub class of the exception listed in the exception clause, then Python will execute that clause and will skip all other clauses. This defeats the purpose of exception clauses, which is to identify and handle exceptions with as much precision as possible.

.. code:: python

    try:
        5 / 0
    except Exception as e:
        print "Exception"
    except ZeroDivisionError as e:  # unreachable code!
        print "ZeroDivisionError"

Best practice
-------------

Move sub class exception clause before its ancestor's clause
............................................................

The modified code below places the ``ZeroDivisionError`` exception clause in front of the ``Exception`` exception clause. Now when the exception is triggered the ``ZeroDivisionError`` exception clause will execute, which is much more optimal because it is more specific.

.. code:: python

    try:
        5 / 0
    except ZeroDivisionError as e:
        print "ZeroDivisionError"
    except Exception as e:
        print "Exception"

References
----------

- Pylint - E0701
