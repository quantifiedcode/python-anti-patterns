Test for object identity should be ``is not``
=============================================

Per the PEP 8 Style Guide, the preferred way to check the identity of an object is ``OBJECT is not CLASS``. Statements that follow the functionally identical but less readable pattern of ``not OBJECT is CLASS`` should be refactored to ``OBJECT is not CLASS``. The problem with ``not OBJECT is CLASS`` is its ambiguity. The statement is executed as ``not (OBJECT is CLASS)``. However, without parentheses it is easy to read it as ``(not OBJECT) is CLASS``, which makes no sense in most contexts.

This is only a guideline. It can be ignored if needed. But the purpose of the PEP 8 style guidelines is to improve the readability of code.

Anti-pattern
------------

The statement below compares an object with the name of ``rectangle`` to a class with the name of ``Circle``. It is evaluated as ``if not (rectangle is Circle)`` but could easily be interpreted as ``if (not rectangle) is Circle``, which probably makes no sense in the context of the program.

.. code:: python

    if not rectangle is Circle

Best practice
-------------

Refactor statement to use ``OBJECT is not CLASS`` pattern
.........................................................

Refactor the statement to the more readable ``OBJECT is not CLASS`` pattern.

.. code:: python

    if rectangle is not Circle

References
----------

- pep8 - E714
- `PEP8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_
