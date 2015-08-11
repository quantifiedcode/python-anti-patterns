Comparing things to `True` the wrong way
========================================

Per the PEP 8 Style Guide, the preferred ways to compare something
to ``True`` are the patterns ``if cond is True:`` or ``if cond:``.
This is only a guideline. It can be ignored if needed.
But the purpose of the PEP 8 Style Guide is to improve the readability of code. 

Anti-pattern
------------

The statement below uses the equality operator to compare a boolean variable to ``True``.
This is not the PEP 8 preferred approach to comparing values to ``True``.
For sure, it is an anti-pattern not only in Python but in almost every programming language.

.. code-block:: python

    flag = True

    if flag == True:  # Not PEP 8's preferred pattern
        print "This works, but is not the preferred PEP 8 pattern for comparing values to True"


Best practices
--------------

Evaluating conditions without comparing to ``True``:
.................................................................

The code below uses the PEP 8 preferred pattern of ``if condition:``.
If the type of the ``condition`` is Boolean, it is obvious that comparing to ``True`` is redundant.
But in Python, every *non-empty* value is treated as true in context of condition checking,
see `Python documentation`_:

  In the context of Boolean operations,
  and also when expressions are used by control flow statements,
  the following values are interpreted as false:
  ``False``, ``None``, numeric zero of all types, and empty strings and containers
  (including strings, tuples, lists, dictionaries, sets and frozensets).
  All other values are interpreted as true.

.. _Python documentation: https://docs.python.org/2/reference/expressions.html#boolean-operations

.. code-block:: python

    flag = True

    if flag:
        print "PEP 8 Style Guide prefers this pattern"

Compare values to ``True`` using the pattern ``if cond is True:``
.................................................................

The code below uses the pattern described in PEP 8 as *worse*:

.. code-block:: python

    flag = True

    if flag is True:
        print "PEP 8 Style Guide prefers this pattern"

This pattern is useful, when you make actual distinction between ``True`` value and
every other that could be treated as true.
The same applies to ``if cond is False``.
This expression is true only if ``cond`` has actual value of ``False``
- not empty list, empty tuple, empty set, zero etc.

References
----------

- pep8 - E712
- `PEP 8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_

Status
------

- No automated check available. `Create it <https://www.quantifiedcode.com/app/patterns>`_ with `Cody <http://docs.quantifiedcode.com/patterns/language/index.html>`_.
