Comparing things to `None` the wrong way
========================================

Per the PEP 8 Style Guide, the preferred way to compare something to ``None`` is the pattern ``if Cond is None``. This is only a guideline. It can be ignored if needed. But the purpose of the PEP 8 style guidelines is to improve the readability of code.

Anti-pattern
------------

The statement below uses the equality operator to compare a variable to ``None``. This is not the PEP 8 preferred approach to comparing values to ``None``.

.. code:: python

    number = None

    if number == None:
        print("This works, but is not the preferred PEP 8 pattern")


Best practice
-------------

Compare values to ``None`` using the pattern ``if cond is None``
.................................................................

The code below uses the PEP 8 preferred pattern of ``if cond is None``.

.. code:: python

    number = None

    if number is None:
        print("PEP 8 Style Guide prefers this pattern")

Here the identity operator ``is`` is used. It will check whether ``number`` is identical to ``None``.
``is`` will return to ``True`` only if the two variables point to the same object.


References
----------

- `PEP 8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_
- `stackoverflow <http://stackoverflow.com/questions/1504717/why-does-comparing-strings-in-python-using-either-or-is-sometimes-produce>`_



