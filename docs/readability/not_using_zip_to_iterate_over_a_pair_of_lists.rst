Not using ``zip()`` to iterate over a pair of lists
===================================================

Summary
-------

``zip()`` is the preferred way to iterate through a pair of lists. Although there are other valid ways to iterate through a pair of lists, this is the most concise way, and in general you can improve code readability by using the method which is most familiar to the most Python programmers.

Description
-----------

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." The preferred way to iterate through a pair of lists is to declare two variables in a loop expression, and then call ``zip(list_one, list_two)``, where ``list_one`` and ``list_two`` are the two lists you wish to iterate through. For each loop iteration, Python will automatically assign the first variable as the next value in the first list, and the second variable as the next value in the second list.

Examples
----------

For loop does not use ``zip()`` to iterate through a pair of lists
..................................................................

The module below defines a variable ``i`` which serves as an index variable for iterating through two lists. Within the for loop the module accesses the corresponding value for each list by using the index variable. This is a common way for iterating through two lists, but it is not the preferred way in python.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]

    for index in range(numbers):
        print numbers[index], letters[index]

Solutions
---------

Use ``zip()`` to iterate through a pair of lists
................................................

The updated module below demonstrates the Pythonic style for iterating through a pair of lists. When the module defines two variables in its ``for`` loop in conjunction with a call to ``zip(numbers, letters)`` on the pair of lists, Python automatically assigns the first variable as the next value in the first list, and the second variable as the next value in the second list.

.. code:: python

    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]

    for numbers_value, letters_value in zip(numbers, letters):
        print numbers_value, letters_value
    
References
----------
- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
