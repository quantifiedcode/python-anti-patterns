Assigning to function call which only returns ``None``
======================================================

Summary
-------

A variable has been assigned to a function which only returns ``None``. This error should be treated as a warning that the assigned function is probably not implemented correctly, since it is rarely useful to assign a function to a variable if the only value the function can return is ``None``.

Description
-----------

When Python raises the ``Assigning to function call which only returns once`` error it usually means that someone forgot to include a ``return`` statement in the function that is being assigned to a variable. When you assign a function to a variable and then call that function via the variable, Python calls the original function and then assigns the value returned by the function to the variable. So when a function only returns ``None`` the only possible value of the variable is ``None``.

There is nothing inherently wrong with assigning a function that can only return ``None`` to a variable. However, it is rarely useful. Therefore, when this error is encountered, you should go back and check the function to ensure that it is impemented as intended.

Examples
----------

Function only returns ``None``
..............................

The variable ``v`` is assigned to the function ``hello``, which prints ``hello`` and then returns ``None``. Note that when ``hello`` is called via ``v`` the ``print "hello"`` statement is not executed.

.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def hello():
        print "hello"
        return None

    v = hello()
    print v # always returns None
    
Note that the ``Assigning to function call which only returns once`` is NOT raised in the following scenario, although it should be.

.. warning:: WARNING! The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    def hello():
        print "hello"
        return  # although this is equivalent to Return None, error is not raised (but it should be)

    v = hello()
    print v # WARNING: always returns None, but error not raised!


Solutions
---------

Modify the function to return values other than ``None``
........................................................

To achieve the desired result of printing "hello" to the screen, the ``hello`` function should return the desired text rather than printing it out within the function definition.

.. code:: python

    def hello():
        return "hello"

    v = hello()
    print v # executes hello() and then assigns the return value of hello() to v

    
References
----------
- `Stack Overflow - Assigning a function to a variable <http://stackoverflow.com/questions/10354163/assigning-a-function-to-a-variable>`_
- `PyLint - W1111 <http://pylint-messages.wikidot.com/messages:w1111>`_
