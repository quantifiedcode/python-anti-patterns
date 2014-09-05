Assigning to function call which only returns none
==================================================

Summary
-------

A variable has been assigned to a function which only returns ``None``. This error should be treated as a warning that the assigned function is probably not implemented correctly, since it is rarely useful to assign a function to a variable if the only value it can return is ``None``.

Description
-----------

Functions that do not contain ``return`` statements return ``None`` by default. When Python raises the ``Assigning to function call which only returns once`` error it usually means that someone forgot to include a ``return`` statement in the function that is being assigned to a variable. There is nothing inherently wrong with using a function that can only return ``None``. However, it is rarely useful. Therefore, when this error is encountered, you should go back and check the function to ensure that it is impemented as intended. 


Examples
----------

Missing ``return`` statement in function
........................................



.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python


Solutions
---------

Description of solution
........................................



.. code:: python

    
References
----------
- `URL Description <URL>`_
