Not using ``iteritems()`` to iterate over a large dictionary
============================================================

`PEP 234 <https://www.python.org/dev/peps/pep-0234://www.python.org/dev/peps/pep-0234/>`_ defines iteration interface for objects. It also states it has significant impact on performance of dict iteration.

Anti-pattern
------------

The code below defines one large dictionary (created with dictionary comprehension) that generates large ammounts of data. When using ``items()`` method, the iteration needs to be completed and stored in-memory before ``for`` loop can begin iterating. The preffered way is to use ``iteritems``. This uses (~1.6GB).

.. code:: python

    d = {i: i * 2 for i in xrange(10000000)}

    # Slow and memory hungry.
    for key, value in d.items():
        print "{} = {}".format(key, value)

Best-practice
-------------

Use ``iteritems()`` to iterate over large dictionary
......................................................

The updated code below uses ``iteritems()`` instead of ``items()`` method. Note how the code is exactly the same, but memory usage is 50% less (~800MB). This is the preferred way to iterate over large dictionaries.

.. code:: python

    d = {i: i * 2 for i in xrange(10000000)}

    # Slow and memory hungry.
    for key, value in d.iteritems():
        print "{} = {}".format(key, value)

References
----------
- `PEP 234 Iterators <https://www.python.org/dev/peps/pep-0234://www.python.org/dev/peps/pep-0234/>`_
