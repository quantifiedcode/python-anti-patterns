Redefinition of unused name
===========================

Summary
-------

Raised when a module redefines a name that is already being used. The object names should be renamed to unique names, or else the module can potentially operate on the wrong object and create strange bugs and unintended behavior.

Description
-----------

The ``redefintion of unused name`` error is frequently encountered when a variable is given the same name as a module. Although not a critical error, using names for more than one purpose has the potential to introduce bugs if the module operates on one object when it was expecting to operate on the other. For this reason the objects should be given unique names unless there is a very strong reason otherwise. Also, overloading names with multiple meanings is confusing in general and can harm code readability.

Examples
----------

Module defines a variable that is the same name as an imported module
.....................................................................

The module below imports the ``json`` module from the Python Standard Library and then creates a variable called ``json`` which stores a list of JSON strings. The program executes successfully, but the ``redefinition of unused name`` error is raised to indicate that the name ``json`` refers to multiple things: in this case a module and a variable.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import json

    json = ['{"first": "John", "last": "Smith"', '"ssn": "613230789"']  # redefinition

    for s in json:
        print s

Solutions
---------

Rename the variable
...................

Often the simplest solution for suppressing the ``redefinition of unused name`` error is to give the objects different, unique names. Because the names are unique, there is no more redefinition taking place, and therefore the error is no longer valid. In the modified module below, the variable storing a list of JSON strings has been changed from ``json`` to ``json_list``.

.. code:: python

    import json

    json_list = ['{"first": "John", "last": "Smith"', '"ssn": "613230789"']  # ok now, unique name

    for s in json_list:
        print s

Delete the earlier references to the name
.........................................

Another way to suppress the ``redefinition of unused name`` error is to remove the earlier statement that references the name. This highly depends on the module, though and may not be a valid solution. In the example above, the ``json`` module from the Python Standard Library wasn't actually being used for anything, so the ``import`` statement could be deleted. Once the ``import json`` statement is deleted there is no longer any redefinition of the ``json`` module so the error is suppressed.

.. code:: python

    json = ['{"first": "John", "last": "Smith"', '"ssn": "613230789"']  # ok now, no more redefinition

    for s in json:
        print s

References
----------
- Pyflakes - F811
