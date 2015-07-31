Not using if/else to switch
==========================

Python doesn't have the ``switch`` statement like Java or C, so sometimes it's common to find
code like this:

Example
-------

.. code:: python

def calculate_with_operator(operator, a, b):

    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '/':
        return a/b
    elif operator == '*':
        return a*b


This is hard to read if the chain of if/else is too long, furthermore it takes a lot of lines
and the program will check a lot of times if the functions was called with the operator "*".

Solutions
-----------
Use a dictionary to do it.
.........................................................

.. code:: pyton

def calculate_with_operator(operator, a, b):

    possible_operators = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b
    }

    return possible_operators[operator]

This is faster and easier to read.
