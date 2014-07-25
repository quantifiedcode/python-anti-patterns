Use of Exec
-----------

Example 

.. sourcecode:: python

    #We load some code from an untrusted source...
    f = open("untrusted_file.py")
    #...and execute it :/
    exec(f.read()) 
