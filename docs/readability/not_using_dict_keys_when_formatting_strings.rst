
Not using dict keys when formatting strings
===========================================

When formatting a string with values from a dictionary, you can use the dictionary keys instead of explicity defining all of the format parameters. Consider this dictionary that stores the name and age of a person.


.. code:: python

    person = {'first':'Tobin', 'age':20}


Anti-pattern
------------

Here is an example of formatting the string with values from the person. This is bad! If we added another key-value pair to the person dictionary, we would have to change the string and the format arguments

.. code:: python

    person = {'first':'Tobin', 'age':20}
    print('{0} is {1} years old'.format(person['first'], person['age']))  # bad
    # >>> Tobin is 20 years old

    person = {'first':'Tobin', 'last': 'Brown', 'age':20}
    print('{0} {1} is {2} years old'.format(person['first'], person['last'], person['age']))  # bad
    # >>> Tobin Brown is 20 years old


Best practice
-------------

By using the dictionary keys in the string we are formatting, the code is much more readable and explicit.

.. code:: python

    person = {'first':'Tobin', 'age':20}
    print('{first} is {age} years old'.format(**person))
    # >>> Tobin is 20 years old

    person = {'first':'Tobin', 'last': 'Brown', 'age':20}
    print('{first} {last} is {age} years old'.format(**person))
    # >>> Tobin Brown is 20 years old


Going even further, the same result can be achieved with your own objects by using ``obj.__dict__``.

.. code:: python

    class Person(object):

        def __init__(self, first, last, age):
            self.first = first
            self.last = last
            self.age = age

        def __str__(self):
            return '{first} {last} is {age} years old'.format(**self.__dict__)


    person = Person('Tobin', 'Brown', 20)
    print(person)
    # >>> Tobin Brown is 20 years old
