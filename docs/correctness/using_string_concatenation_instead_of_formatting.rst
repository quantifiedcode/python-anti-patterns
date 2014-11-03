Using string concatenation instead of formatting
================================================

Summary
-------

Although string concatentation is significantly faster than string formatting, the Python community finds formatting to be much more readable. Therefore, when performance is not an issue (or formatting is required) choose string formatting over string concatenation.

Description
-----------

The Python community places a high premium on readable code. PEP 20 states that "Readability counts." Although string concatenation performs better than string formatting you should use string formatting because it is generally agreed to be more readable.

Examples
----------

Using string concatenation
..........................

The simple module below uses string concatenation to print out some text. String concatenation is generally not the preferred way to join strings in Python.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    name = "Fred"

    print "Hello, my name is " + name + "."

Solutions
---------

Use string formatting
.....................

The modified module below prints out the same message, this time using string formatting, which is the preferred method in the Python community for joining strings.

.. code:: python

    name = "Fred"

    print "Hello, my name is {:s}".format(name)
    
References
----------
- `Stack Overflow - String Concatenation vs. String Substitution <http://stackoverflow.com/questions/376461/string-concatenation-vs-string-substitution-in-python>`_
