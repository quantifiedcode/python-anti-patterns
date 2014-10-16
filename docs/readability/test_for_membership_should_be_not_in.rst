Test for membership should be ``not in``
========================================

Summary
-------

Raised when a statement contains the syntax ``not VALUE in SEQUENCE``. The statement should be refactored to ``VALUE not in SEQUENCE`` to improve readability.

Description
-----------

Per the PEP 8 Style Guide, the preferred way to check if a value is contained in a sequence is ``VALUE not in SEQUENCE``. Statements that follow this syntax should be refactored to ``VALUE not in SEQUENCE``. The two statements are equivalent, but ``VALUE not in SEQUENCE`` is more readable. The problem with the statement is its ambiguity. The statement is executed as ``not (VALUE in SEQUENCE)``. However, without parentheses somebody may read it as ``(not VALUE) in SEQUENCE``, which makes no sense in most contexts. 

This is only a guideline. It can be ignored if needed. But the purpose of the PEP 8 style guidelines is to improve the readability of code.

Examples
----------

Statement uses ``not VALUE in SEQUENCE`` pattern
................................................

The ``print`` statement below uses the pattern ``not VALUE in SEQUENCE`` to test if a number is in a list. Although this is valid syntax, the statement is confusing. 

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    target = 3
    sequence = [1, 2, 3, 4, 5]
    
    print not target in sequence  # Confusing. Does it evaluate to (not target) in sequence
                                  # or not (target in sequence)?
    # FYI: prints "False" because the target value is indeed a 
    # member of the sequence. So it evaluates to not (target in sequence).

Solutions
---------

Refactor statement to use ``VALUE not in SEQUENCE`` pattern
...........................................................

Refactor the statement to the more readable ``VALUE not in SEQUENCE`` pattern.

.. code:: python

    target = 3
    sequence = [1, 2, 3, 4, 5]
    
    print target not in sequence  # more readable
    # FYI: still prints "False"
    
References
----------
- `PEP8 Style Guide - Programming Recommendations <http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations>`_
- `Stack Overflow - What is more 'pythonic' for 'not'? <http://stackoverflow.com/questions/17659303/what-is-more-pythonic-for-not>`_
- pep8 - E713
