Use new ``raise`` syntax
========================

Summary
-------

The module uses the old ``raise`` syntax ``raise ErrorClass, args``. Use the new raise syntax ``raise ErrorClass(args)`` to improve readability and ensure compatibility with Python versions 3 and above (which require the new syntax).

Description
-----------

One of Python's guiding maxims is "there should be one obvious way to do it." Providing multiple, functionally-equivalent ways to raise exceptions violates this maxim. 

Examples
----------

Module uses old ``raise`` syntax
................................

The module below triggers the ``use new raise syntax`` error because of the statement ``raise Exception, "1 != 0"``. This syntax is deprecated in Python 3.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    try:
        if 1 != 0:
            raise Exception, "1 != 0"  # old raise syntax
    except Exception as e:
        print e

Solutions
---------

Use the new ``raise`` syntax
............................

The updated module has replaced the old style ``raise`` statement ``raise Exception, "1 != 0"`` with the new style ``raise Exception("1 != 0")``. The two statements are equivalent.

.. code:: python

    try:
        if 1 != 0:
            raise Exception("1 != 0")  # new raise syntax
    except Exception as e:
        print e

References
----------
- `PEP 3109 - Raising Exceptions in Python 3 <http://legacy.python.org/dev/peps/pep-3109/>`_
- PyLint - W0121
