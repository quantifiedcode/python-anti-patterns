Not using ``zip()`` to iterate over a pair of lists
===================================================

`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_ states "There should be one-- and preferably only one --obvious way to do it." The preferred way to iterate through a pair of lists is to declare two variables in a loop expression, and then call ``zip(list_one, list_two)``, where ``list_one`` and ``list_two`` are the two lists you wish to iterate through. For each loop iteration, Python will automatically assign the first variable as the next value in the first list, and the second variable as the next value in the second list.

Anti-pattern
------------

The code below defines a variable ``index`` which serves as an index variable for iterating through two lists. Within the for loop the code accesses the corresponding value for each list by using the index variable. This is a common way for iterating through two lists, but it is not the preferred way in Python.

.. code:: python

    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]

    for index in range(len(numbers)):
        print numbers[index], letters[index]

Best-practice
-------------

Use ``zip()`` to iterate through a pair of lists
................................................

The updated code below demonstrates the Pythonic style for iterating through a pair of lists. When the code defines two variables in its ``for`` loop in conjunction with a call to ``zip(numbers, letters)`` on the pair of lists, Python automatically assigns the first variable as the next value in the first list, and the second variable as the next value in the second list.

.. code:: python

    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]

    for numbers_value, letters_value in zip(numbers, letters):
        print numbers_value, letters_value

References
----------

- `PEP 20 - The Zen of Python <http://legacy.python.org/dev/peps/pep-0020/>`_
- `Built-in Functions > zip(*iterables) <https://docs.python.org/3.4/library/functions.html#zip>`_
