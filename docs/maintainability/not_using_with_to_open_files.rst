Not using ``with`` to open files
================================

In Python 2.5, the ``file`` class was equipped with special methods that are automatically called whenever a file is opened via a ``with`` statement (e.g. ``with open("file.txt", "r") as file``). These special methods ensure that the file is properly and safely opened and closed.

Anti-pattern
------------

The code below does not use ``with`` to open a file. This code depends on the programmer remembering to manually close the file via ``close()`` when finished. Even if the programmer remembers to call ``close()`` the code is still dangerous, because if an exception occurs before the call to ``close()`` then ``close()`` will not be called and the memory issues can occur, or the file can be corrupted.

.. code:: python

    f = open("file.txt", "r")
    content = f.read()
    1 / 0  # ZeroDivisionError
    # never executes, possible memory issues or file corruption
    f.close()

Best practice
-------------

Use ``with`` to open a file
...........................

The modified code below is the safest way to open a file. The ``file`` class has some special built-in methods called ``__enter__()`` and ``__exit__()`` which are automatically called when the file is opened and closed, respectively. Python guarantees that these special methods are always called, even if an exception occurs.

.. code:: python

    with open("file.txt", "r") as f:
        content = f.read()
        # Python still executes f.close() even though an exception occurs
        1 / 0 

References
----------

`effbot - Understanding Python's with statement <http://effbot.org/zone/python-with-statement.htm>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/7a20886d210e4cdaa38a7e3e9fe9b9a3>`_
