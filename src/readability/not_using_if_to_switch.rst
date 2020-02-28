Do not use if/else to switch
==========================

Python doesn't have the ``switch`` statement like Java or C, so sometimes it's common to find
code like this:

Anti-Pattern
------------

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

Best Practice
-------------

Use a dictionary to do it
.........................

.. code:: pyton

def calculate_with_operator(operator, a, b):

    possible_operators = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b
    }

    return possible_operators[operator](a,b)

This is faster and easier to read.
It should be noted that the lambda functions are necessary here to increase performance.
Without them the method returns the correct result but it will evaluate every value of the dictionary regardless of the given operator
In this case the difference in speed will be barely noticeable but can become critical if some more elaborate equations need to be solved.
