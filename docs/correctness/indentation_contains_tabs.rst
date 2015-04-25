Indentation contains tabs
=========================

Per the PEP 8 Style Guide, all Python code should be consistently indented with 4 spaces for each level of indentation, not tabs.

Anti-pattern
------------

The following code uses tabs for indentation. Python code should be indented with four spaces for each level of indentation.

.. code:: python

    def print_hello_world():
          print "Hello, World!"  # indented with tab
    def print_goodbye_world():
        print "Goodbye, World!"  # indented with tab

Best practice
-------------

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
- pep8 - W191
