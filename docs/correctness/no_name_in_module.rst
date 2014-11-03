No name in module
=================

Summary
-------

The imported module has no publicly available member with this name. Fix the import statement or remove any references to the non-existent name or else Python will raise an ``ImportError`` and the program will not successfully execute.

Description
-----------

This error is commonly encountered when somebody makes a typo in the name of the imported member module, or the module has not publicly exposed the member for public use.

Examples
----------

Typo in import statement
........................

The module ``b`` attempts to implement a constant from module ``a`` called ``HI``. There is no such name in module ``a``. The author who wrote the import statement made a typo; the member he wants is called ``HELLO``. This import statement causes the ``no name in module`` error. Module ``b`` will encounter a ``ImportError`` runtime error when this code is executed.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    """a.py"""
    HELLO = "Hello, World!"

    """b.py"""
    from a import HI  # ImportError: no name "HI" in module "a"

Solutions
---------

Fix the import statement typo
.............................

After reviewing the code, the author realizes that he has made a typo in his import statement. The member that he wants to import is called ``HELLO``, not ``HI``. After changing the import statement in module ``b`` the ``no name in module`` error is suppressed.

.. code:: python

    """a.py"""
    HELLO = "Hello, World!"

    """b.py"""
    from a import HELLO
    
References
----------
- `PyLint - E0611 <http://pylint-messages.wikidot.com/messages:e0611>`_
