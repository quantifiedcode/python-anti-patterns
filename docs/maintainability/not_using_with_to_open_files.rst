Not using ``with`` to open files
================================

Summary
-------

Use a ``with`` statement to open a file (e.g. ``with open("file.txt", "r" as f``). This is the standard and safest way to open a file in Python.

Description
-----------

In Python 2.5, the ``file`` class was equipped with special methods that are automatically called whenever a file is opened via a ``with`` statement (e.g. ``with open("file.txt", "r") as file``). These special methods ensure that the file is properly and safely opened and closed.

Examples
----------

Not using ``with`` to open a file
.................................

The module below does not use ``with`` to open a file. This code depends on the programmer remembering to manually close the file via ``close()`` when finished. Even if the programmer remembers to call ``close()`` the code is still dangerous, because if an exception occurs before the call to ``close()`` then ``close()`` will not be called and the memory issues can occur, or the file can be corrupted.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    f = open("file.txt", "r")
    content = f.read()
    1 / 0  # ZeroDivisionError
    f.close()  # never executes, possible memory issues or file corruption

Solutions
---------

Use ``with`` to open a file
...........................

The modified module below is the safest way to open a file. The ``file`` class has some special built-in methods called ``__enter__()`` and ``__exit__()`` which are automatically called when the file is opened and closed, respectively. Python guarantees that these special methods are always called, even if an exception occurs.

.. code:: python

    with open("file.txt", "r") as f:
        content = f.read()
        1 / 0  # Python still executes f.close() even though an exception occurs
    
References
----------
`effbot - Understanding Python's with statement <http://effbot.org/zone/python-with-statement.htm>`_
