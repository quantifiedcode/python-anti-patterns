__init__ method from base class %r not called
=============================================

Summary
-------

A derived class should always call the ``__init__`` method of its base class in its own ``__init__`` method. Forgetting to call the base class' ``__init__`` method could leave instance members of the base class uninitialized. This can introduce bugs in a program if the derived class attempts to use any of the uninitialized instance members from the base class.

Description
-----------

If a derived class does not call its base class' ``__init__`` method and then attempts to access any instance members defined in the base class, any or all of these instance members could potentially be undefined, depending on how the base class is implemented. Since it is highly likely that the derived class will sooner or later need to access one of the base class instance members, the derived class should always call the base class' ``__init__`` method in its own ``__init__`` method. Unless there is a very good reason for doing otherwise, this should be the very first statement in the derived class' ``__init__`` method.

Examples
----------

Derived class does not call base class' ``__init__`` method
...........................................................

.. code:: python

    class Person:
        def __init__(self, first_name):
            self.first_name = first_name
        def get_first_name(self):
            return self.first_name

    class Male(Person):
        def __init__(self, first_name):
            self.gender = "male"
        def get_gender(self):
            return self.gender

    m = Male("Ford")
    print "first name: %s" % m.get_first_name() # Runtime error! See output below.
    
    # Traceback (most recent call last):
    #  File "w0231.py", line 15, in <module>
    #    print "first name: %s" % m.get_first_name()
    #  File "w0231.py", line 5, in get_first_name
    #    return self.first_name
    # AttributeError: Male instance has no attribute 'first_name'

Solutions
---------

Call the base class' ``__init__`` method
........................................

.. code:: python

    class Person:
        def __init__(self, first_name):
            self.first_name = first_name
        def get_first_name(self):
            return self.first_name

    class Male(Person):
        def __init__(self, first_name):
            Person.__init__(self, first_name)
            self.gender = "male"
        def get_gender(self):
            return self.gender

    m = Male("Ford")
    print "first name: %s" % m.get_first_name() # "name: Ford"
    
References
----------
- `PyLint - W0231 <http://pylint-messages.wikidot.com/messages:w0231>`_
