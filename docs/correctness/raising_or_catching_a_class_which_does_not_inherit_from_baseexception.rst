Raising or catching a class which does not inherit from ``BaseException``
=========================================================================

Summary
-------

The module is attempting to raise and catch a class which does not inherit from ``BaseException``. Either do not raise the class as an exception or modify the class to inherit from ``Exception``. If Python encounters this it will raise ``TypeError`` at runtime and the module will not successfully execute.

Description
-----------

Classes used for handling and representing exceptions must always inherit from ``BaseException``. User-defined exception classes should actually inherit from ``Exception``; they shouldn't directly inherit from ``BaseException``. Python requires all exception classes to inherit from a base exception superclass to ensure that they all meet the minimum required interface needed to be useful.

Examples
----------

Raising class that does not inherit from ``BaseException``
..........................................................

The module below defines a class ``MyException`` and then attempts to raise this as an exception. Python raises a ``TypeError`` when it encounters this code because all classes raised as exceptions must inherit from ``BaseException``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class MyException(object):  # doesn't inherit from BaseException
        def __init__(self, code, message):
            self.code = code
            self.message = message

    try:
        if 1 != 0:
            raise MyException(1244, "1 != 0 Exception")
    except MyException as e:
        print e.message


Solutions
---------

Modify the class to inherit from ``BaseException``
..................................................

In the modified module below the user-defined exception class has been modified to inherit from ``BaseException``. The class actually inherits from ``Exception``, which in turn inherits from ``BaseException``. User-defined exception classes should never inherit directly from ``BaseException``.

.. code:: python

    class MyException(Exception):  # inherits from Exception now
        def __init__(self, code, message):
            self.code = code
            self.message = message

    try:
        if 1 != 0:
            raise MyException(1244, "1 != 0 Exception")
    except MyException as e:
        print e.message # 1 != 0 Exception
    
Do not raise the class as an exception
......................................

If the raised class cannot be modified, then the class should not be raised to handle exceptions. In the modified module below the module now raises ``Exception`` instead of ``MyException``.

.. code:: python

    class MyException(Exception):  # inherits from Exception now
        def __init__(self, code, message):
            self.code = code
            self.message = message

    try:
        if 1 != 0:
            raise Exception("Exception: 1 != 0")
    except Exception as e:
        print e # 1 != 0 Exception

References
----------
- PyLint - E0710
- PyLint - E0712
- `Python Standard Library - Exceptions <https://docs.python.org/2/library/exceptions.html>`_
- `PEP 352 - Required Superclass for Exceptions <http://legacy.python.org/dev/peps/pep-0352/>`_
