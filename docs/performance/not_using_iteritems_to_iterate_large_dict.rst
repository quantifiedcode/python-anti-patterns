Not using ``iteritems()`` to iterate over a large dictionary
============================================================

`PEP 234 <https://www.python.org/dev/peps/pep-0234://www.python.org/dev/peps/pep-0234/>`_ defines iteration interface for objects. It also states it has significant impact on performance of dict iteration.

.. note:: This anti-pattern only applies to Python versions 2.x. In Python 3.x ``items()`` returns an iterator (consequently, ``iteritems()`` has been removed from Python 3.x).


Anti-pattern
------------

The code below defines one large dictionary (created with dictionary comprehension) that generates large amounts of data. When using ``items()`` method, the iteration needs to be completed and stored in-memory before ``for`` loop can begin iterating. The prefered way is to use ``iteritems``. This uses (~1.6GB).

.. code:: python

    d = {i: i * 2 for i in xrange(10000000)}

    # Slow and memory hungry.
    for key, value in d.items():
        print("{0} = {1}".format(key, value))

Best-practice
-------------

Use ``iteritems()`` to iterate over large dictionary
....................................................

The updated code below uses ``iteritems()`` instead of ``items()`` method. Note how the code is exactly the same, but memory usage is 50% less (~800MB). This is the preferred way to iterate over large dictionaries.

.. code:: python

    d = {i: i * 2 for i in xrange(10000000)}

    # Memory efficient.
    for key, value in d.iteritems():
        print("{0} = {1}".format(key, value))

References
----------
- `PEP 234 Iterators <https://www.python.org/dev/peps/pep-0234/>`_

Status
------

- No automated check available. `Create it <https://www.quantifiedcode.com/app/patterns>`_ with `Cody <http://docs.quantifiedcode.com/patterns/language/index.html>`_.
