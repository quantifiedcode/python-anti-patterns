Parameter passed as both positional and keyword argument
========================================================

Summary
-------

A positional and keyword parameter have the same name. Make the names unique in the function defintion or else Python will raise a ``TypeError`` and the module will not execute.

Description
-----------

When a positional and keyword parameter in a function definition have the same name, Python cannot resolve which parameter is being referenced when the function is called.

Examples
----------

A positional and keyword parameter have the same name
.....................................................

In the ``print_string`` function below, the first parameter is a positional parameter. The second parameter indicates that the function accepts keyword arguments (each keyword argument is accessed via ``keyword_arguments["name"]`` where name is the keyword passed when the function is called. Because this function has a positional parameter called ``string`` and it also accepts a keyword argument called ``string``, the ``Parameter passed as both positional and keyword argument`` error is raised.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def print_string(string, **keyword_arguments):
        print string
        print keyword_arguments["string"]

    print_string("positional", string="keyword")  # can't resolve which string is referenced

Solutions
---------

Make parameter names unique
...........................

The modified module below resolves the problem by making the parameter names unique.

.. code:: python

    def print_string(positional_argument, **keyword_arguments): # changed name of first parameter
        print positional_argument 
        print keyword_arguments["string"]

    print_string("positional", string="keyword")  # no ambiguity now
    
References
----------
