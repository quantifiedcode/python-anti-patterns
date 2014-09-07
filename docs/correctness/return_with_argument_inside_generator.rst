Return with argument inside generator
=====================================

Summary
-------

Raised when a generator contains a ``return`` statement. The ``return`` statement should be removed or modified to return nothing (e.g. ``return`` or ``return None``) or else a ``SyntaxError`` runtime error will occur when the generator is used.

Description
-----------

A generator can only contain a ``return`` statement if it returns ``None``. In other words, the only two valid ``return`` statements in a generator are ``return`` and ``return None``. Python will raise a ``SyntaxError`` runtime error if the generator returns any other value.

Examples
--------

Generator contains ``return`` statement that returns something other than ``None``
..................................................................................

The ``tokenize`` function below is a generator because it contains the ``yield`` statement and iterates over a string. ``tokenize`` violates Python's generator protocol because it contains a ``return`` statement that returns a value other than ``None``.

.. code:: python

    def tokenize(string):
        for token in string.split(' '):
            yield token
            return "I break everything."  # generator cannot return anything other than None

    for t in tokenize("This sentence has five tokens."):
        print t

Solutions
-----------

Remove the ``return`` statement
...............................

Remove the ``return`` statement from the generator if it is not needed.

.. code:: python

    def tokenize(string):
        for token in string.split(' '):
            yield token
            # return statement removed

    for t in tokenize("This sentence has five tokens."):
        print t

Modify the ``return`` statement to return ``None``
..................................................

If the ``return`` statement is needed in the generator, modify it to return ``None``.

.. code:: python

    def tokenize(string):
        for token in string.split(' '):
            yield token
            return None

    for t in tokenize("This sentence has five tokens."):
        print t

References
----------

- `PyLint - E0106 <http://pylint-messages.wikidot.com/messages:e0106>`_
- `Stack Overflow - Python SyntaxError: (“'return' with argument inside generator”) <http://stackoverflow.com/questions/15809296/python-syntaxerror-return-with-argument-inside-generator>`_
