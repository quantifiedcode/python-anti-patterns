use of exec
^^^^^^^^^^^

While not a security problem per se, using the `exec` statement is considered dangerous
(and unclean) and should be avoided whenever possible.

Example
"""""""

.. sourcecode:: python

    #We load some code from an untrusted source...
    f = open("untrusted_file.py")
    #...and execute it :/
    exec(f.read()) 

Alternatives
""""""""""""

