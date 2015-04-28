Dynamically creating variable/method/function names
===================================================

Sometimes programmer gets and idea to make his/hers work easier by creating magically working code that uses ``setattr()`` and ``getattr()`` functions to set some variable. This may look like a good idea, because there is no need to write all the methods by hand. However you're asking for trouble down the road.


Example
-------

Consider following code. You have some data and want to update the *class* with all of the data. Of course you don't want to do this by hand, especially if there is tons of items in ``data_dict``. However when refactoring this kind of code after several years, and you'd like to know where is some variable added to this class, you'd usually use ``grep`` or ``ack_grep`` to find it. But when setting variables/methods/functions like this, you're screwed.

.. code:: python

    data_dict = {'var1': 'Data1', 'var2': 'Data2'}


    class MyAwesomeClass:

        def __init__(self, data_dict):
            for key, value in data_dict.iteritems():
                setattr(self, key, value)


While previous example may look easy to find and debug, consider this:

.. code:: python

    data_list = ['dat1', 'dat2', 'dat3']
    data_dict = {'dat1': [1, 2, 3], 'dat2': [4, 5, 6], 'dat3': [7, 8, 9], 'dat4': [0, 4, 6]}

    class MyAwesomeClass:

        def __init__(self, data_list, data_dict):
            counter = 0

            for key, value in data_dict.iteritems():
                if key in data_list:
                    setattr(self, key, value)
                else:
                    setattr(self, 'unknown' + str(counter), value)
                    counter += 1


Now the class contains also ``unknownX`` variables indexed by their count. Well, what a nice mess we created here. Try to find a year later where these variables come from.


Solutions
---------

Find another way
................

While the approach in examples abowe may be easiest to write, it is the worst to maintain later. You should always try to find another way to solve your problem.

Typical examples:

* Use function to parse incomming data
* Use the data dict/list itself without class

This however depends on the task at hand.
