use of eval
^^^^^^^^^^^

Similar to the `exec` statement, the `eval()` function can allow execution of unsafe code.

When using it, you should make sure to only evaluate code from known, trustworthy sources and
treat return values with special care.

Example
"""""""

.. sourcecode:: python

    #We load some code from an untrusted source...
    f = open("untrusted_file.py")
    #We read a line from the file
    str = f.readline()
    #...and evaluate it
    eval(str) 

Alternatives
""""""""""""

For configuration settings, use YAML or JSON instead. If more complex logic is required,
consider defining a domain-specific-language (DSL) instead.

The ***** module can help you to restrict the types of statements that should be evaluated,
altough it does not provide absolute safety.
