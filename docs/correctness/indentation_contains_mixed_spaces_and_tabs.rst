Indentation contains mixed spaces and tabs
==========================================

Summary
-------

The code is being indented with both spaces and tabs. Python code should be indented with 4 spaces.

Description
-----------

Per the PEP 8 Style Guide, all Python code should be consistently indented with 4 spaces, not tabs.

Examples
----------

Code is indented with spaces and tabs
.....................................

The following code mixes spaces and tabs for indentation. The ``print "Hello, World!" statement is indented with a tab. The rest of the code is indented with 4 spaces.

.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_hello_world():
		print "Hello, World!"  # indented with tab
    def print_goodbye_world():
        print "Goodbye, World!"

Solutions
---------

Consistently indent with spaces
...............................

All Python code should be consistently indented with 4 spaces.

.. code:: python

    def print_hello_world():
		print "Hello, World!"  # indented with tab
    def print_goodbye_world():
        print "Goodbye, World!"  # indented with 4 spaces

    
References
----------
- `PEP 8 - Tabs or Spaces? <http://legacy.python.org/dev/peps/pep-0008/#tabs-or-spaces>`_
- `PEP 8 - Indentation <http://legacy.python.org/dev/peps/pep-0008/#indentation>`_
