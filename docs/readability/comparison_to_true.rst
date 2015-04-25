Comparing things to `True` the wrong way
========================================

Per the PEP 8 Style Guide, the preferred ways to compare something to ``True`` are the patterns ``if cond is True:`` or ``if cond:``. This is only a guideline. It can be ignored if needed. But the purpose of the PEP 8 Style Guide is to improve the readability of code.

Anti-pattern
------------

The statement below uses the equality operator to compare a boolean variable to ``True``. This is not the PEP 8 preferred approach to comparing values to ``True``.

.. code:: python

    flag = True

    if flag == True:  # Not PEP 8's preferred pattern
        print "This works, but is not the preferred PEP 8 pattern for comparing values to True"


Best practices
--------------

Compare values to ``True`` using the pattern ``if cond is True:``
.................................................................

The code below uses the PEP 8 preferred pattern of ``if cond is True:``.

.. code:: python

    flag = True

    if flag is True:
        print "PEP 8 Style Guide prefers this pattern"

Compare values to ``True`` using the pattern ``if cond:``
.................................................................

The code below uses the PEP 8 preferred pattern of ``if cond:``. This only works if the object, variable, or expression evaluates to a Boolean value of ``True`` or ``False``.

.. code:: python

    flag = True

    if flag:
        print "PEP 8 Style Guide prefers this pattern"

References
----------

- pep8 - E712
- `PEP 8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_
