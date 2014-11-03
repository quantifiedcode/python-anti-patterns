Raising unallowed type
======================

Summary
-------

The ``Raising %s while only classes, instances or string are allowed`` error is encountered when a ``raise`` statement contains a type other than a class, instance, or string. These three object types are the only things that can be raised. Python raises a ``TypeError`` at runtime if this problem is not fixed.

Description
-----------

A ``raise`` statement must raise a valid exception type. This can be either a class, instance, or string.

Examples
----------

Module raises ``False``
.......................

The module attempts to raise ``False`` when a function does not execute as expected. ``False`` is not a valid exception type, so Python raises a ``TypeError`` at runtime when it encounters this code.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def equals(a, b):
        if a != b:
            raise False  # causes TypeError

Solutions
---------

Raise a valid exception type
............................

The object type proceeding the ``raise`` keyword should be a class, instance, or string. The modified module below suppresses the ``Raising %s while only classes, instances or string are allowed`` error by modifying the ``raise`` statement to raise a valid exception type, in this case ``Warning``.

.. code:: python

    def equals(a, b):
        if a != b:
            raise Warning  # ok now, valid exception type

References
----------
- PyLint - E0702
