Test for object identity should be ``is``
========================================

Testing the identity of two objects can be achieved in python with a special operator called ``in``.
Most prominently it is used to check whether an variable points to ``None``.
But the operator can examine any kind of identity.
This often leads to confusion because equality of two different objects will return ``False``.

Anti-pattern
------------

.. code:: python

    a = range(10)
    b = range(10)

    print((a is b))

This code snippet will print ``False`` even though ``a`` and ``b`` have equal values.
This can occur because ``a`` and ``b`` are references that point to different objects which happen to have the same value.
To verify the equality of two variables the ``==`` operator should be used.

Best practice
-------------

Only use the ``is`` operator if you want to check the exact identity of two references.

.. code:: python

    some_list = None

    if some_list is None:
        do_somthing_with_the_list()

References
----------

- `PEP8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_

Status
------

- No automated check available. `Create it <https://www.quantifiedcode.com/app/patterns>`_ with `Cody <http://docs.quantifiedcode.com/patterns/language/index.html>`_.
