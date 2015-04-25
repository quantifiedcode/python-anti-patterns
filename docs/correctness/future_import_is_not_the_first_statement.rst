``__future__`` import is not the first non-docstring statement
==============================================================

The ``__future__`` module enables a module to use functionality that is mandatory in future Python versions. If it was possible to place the ``__future__`` module in the middle of a module, then that would mean that one half of the module could use the old Python functionality for a given feature, and the other half (after the ``__future__`` import) could use the new Python functionality of the feature. This could create many strange and hard-to-find bugs, so Python does not allow it.

Anti-pattern
------------

The code below attempts to place a ``__future__`` import statement in the middle of the module. When Python encounters the ``from __future__ import division`` statement it raises a ``SyntaxError`` and halts execution. However, if the code were to execute, the first ``print`` statement would print out ``1`` (which is how the division operator behaves in Python versions 2 and below), but the second ``print`` statement would print out a decimal value, which is how the division operator functions in Python versions 3 and later. As you can see, this could create very strange behavior, so Python does not allow ``__future__`` import statements in the middle of a module. The module can use either version of the division operator, but it can't use both.

.. code:: python

    print 8 / 7  # 1

    from __future__ import division  # SyntaxError

    print 8 / 7  # 1.1428571428571428

Best practice
-------------

Remove ``__future__`` import
............................

In the modified code below, the author decides that the module needs to use the old functionality of the division operator. The only solution in this case is to remove the ``__future__`` import statement from the module.

.. code:: python

    # removed __future__ import statement

    print 8 / 7  # 1

Place ``__future__`` import before all other statements
.......................................................

In the modified code below, the author decides that the module needs the new functionality of the division operator. The only solution then is to place the ``__future__`` import statement at the beginning of the module

.. code:: python

    from __future__ import division

    print 8 / 7  # 1.1428571428571428

References
----------

- PyLint - W0410
- `Simeon Visser - How does 'from __future__ import ...' work? <http://simeonvisser.com/posts/how-does-from-future-import-work-in-python.html>`_
- `Python Standard Library - __future__ <https://docs.python.org/2/library/__future__.html>`_
