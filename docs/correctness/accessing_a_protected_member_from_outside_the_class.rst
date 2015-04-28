Accessing a protected member from outside the class
===================================================

Accessing a protected member (a member prefixed with ``_``) of a class from outside that class usually
calls for trouble, since the creator of that class did not intend this function to be exposed.

Anti-pattern
------------

.. code:: python

    class Rectangle(object):
        def __init__(self, width, height):
            self._width = width
            self._height = height

    r = Rectangle(5, 6)
    print "Width: {:d}".format(r._width)  # direct access of protected member

Best practice
-------------

If you are absolutely sure that you need to call the proteced function from the outside,
do the following:

 * Make sure that calling the function from outside the class does not cause any inadverent side effects.
 * Refactor it such that it becomes part of the public interface of the class.

References
----------

- PyLint - W0212
