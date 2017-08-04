Accessing a protected member from outside the class
===================================================

Accessing a protected member (a member prefixed with ``_``) of a class from outside that class usually
calls for trouble, since the creator of that class did not intend this member to be exposed.

Anti-pattern
------------

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self._width = width
            self._height = height

    r = Rectangle(5, 6)
    # direct access of protected member
    print("Width: {:d}".format(r._width))

Best practice
-------------

If you are absolutely sure that you need to access the protected member from the outside,
do the following:

 * Make sure that accessing the member from outside the class does not cause any inadvertent side effects.
 * Refactor it such that it becomes part of the public interface of the class.

References
----------

- PyLint - W0212, protected-access


