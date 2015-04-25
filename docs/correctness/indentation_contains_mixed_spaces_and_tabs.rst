Indentation contains mixed spaces and tabs
==========================================

Per the PEP 8 Style Guide, all Python code should be consistently indented with 4 spaces, never tabs.

Anti-pattern
------------

The following code mixes spaces and tabs for indentation. The ``print "Hello, World!"`` statement is indented with a tab. The ``print "Goodybye, World!"`` statement is indented with 4 spaces.

.. code:: python

    def print_hello_world():
	print "Hello, World!"  # indented with tab
    def print_goodbye_world():
        print "Goodbye, World!"  # indented with 4 spaces

Solutions
---------

Consistently indent with spaces
...............................

All Python code should be consistently indented with 4 spaces.

.. code:: python

    def print_hello_world():
        print "Hello, World!"  # indented with 4 spaces
    def print_goodbye_world():
        print "Goodbye, World!"  # indented with 4 spaces


References
----------

- `PEP 8 Style Guide - Tabs or Spaces? <http://legacy.python.org/dev/peps/pep-0008/#tabs-or-spaces>`_
- `PEP 8 Style Guide - Indentation <http://legacy.python.org/dev/peps/pep-0008/#indentation>`_
- pep8 - E731
