Asking for permission instead of forgiveness
============================================

The Python community uses an EAFP (easier to ask for forgiveness than permission) coding style. This coding style assumes that needed variables, files, etc. exist. Any problems are caught as exceptions. This results in a generally clean and concise style containing a lot of ``try`` and ``except`` statements.

Anti-pattern
------------

The code below uses an ``if`` statement to check if a file exists before attempting to use the file. This is not the preferred coding style in the  Python community. The community prefers to assume that a file exists and you have access to it, and to catch any problems as exceptions.

.. code:: python

    import os

    # violates EAFP coding style
    if os.path.exists("file.txt"):
        os.unlink("file.txt")

(Beyond coding style, the above code also has a potential race condition, as another program might delete the file between the ``exists`` and ``unlink`` calls.)

Best practice
-------------

Assume the file can be used and catch problems as exceptions
.............................................................

The updated code below is a demonstration of the EAFP coding style, which is the preferred style in the Python community. Unlike the original code, the modified code below simply assumes that the needed file exists, and catches any problems as exceptions. For example, if the file does not exist, the problem will be reported as a ``FileNotFoundError`` exception.

In Python 2, a plain ``OSError`` is raised instead (which can also result from other errors, e.g. permission issues).

.. code:: python

    import os

    try:
        os.unlink("file.txt")
    # raised when file does not exist
    except FileNotFoundError: # or OSError, if using Python 2
        pass

References
----------

- `Python 3 - Glossary: EAFP <https://docs.python.org/3/glossary.html#term-eafp>`_


