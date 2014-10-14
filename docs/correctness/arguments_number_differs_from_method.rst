Arguments number differs from method
====================================

Summary
-------

A child class has implemented an abstract method with a different number of arguments than what is defined in the parent class' method signature. Treat this as a warning. The child class' implementation should match the argument signature defined in the the parent class.

Description
-----------

If the child class' implementation of the parent class' abstract method contains more arguments than the method signature in the parent class, Python will be able to execute the method. If the child class' implementation has less arguments than what is defined in the parent class' abstract method signature, then Python will not be able to execute the method. Either way, this defeats the purpose of abstract methods. Abstract methods are contracts passed down to inherited classes which signify that the parent class expects its children to implement a method that matches a particular argument signature. When the child class does not match the signature defined in the parent class, it is not fulfilling its part of the inheritance contract.

Examples
----------

Child class method contains more arguments than parent class' method signature
..............................................................................

In the module below ``Dog`` is a child class of ``Animal``. ``Dog`` is supposed to implement a class called ``print_class_information`` that takes no arguments. However, ``Dog``'s implementation accepts one argument, ``biological_family``.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    import abc

    class Animal(object):
        __metaclass__ = abc.ABCMeta

        def __init__(self, number_of_legs):
            self.number_of_legs = number_of_legs

        @abc.abstractmethod
        def print_class_information(self):
            return

    class Dog(Animal):
        def __init__(self):
            Animal.__init__(self, 4)
        def print_class_information(self, biological_family):  # signature does not match Animal's
            print "Biological Family: {:s}".format(biological_family)
            print "Class Name: Dog"

    d = Dog()
    d.print_class_information("Canidae")

Solutions
---------

Implement the child class method to match the parent class signature
....................................................................

In the modified module below, the ``Dog`` class has removed the second argument from the ``print_class_information()`` method signature. The method now matches the signature defined in ``Animal``.

.. code:: python

    import abc

    class Animal(object):
        __metaclass__ = abc.ABCMeta

        def __init__(self, number_of_legs):
            self.number_of_legs = number_of_legs

        @abc.abstractmethod
        def print_class_information(self):
            return

    class Dog(Animal):
        def __init__(self):
            Animal.__init__(self, 4)
        def print_class_information(self):  # signature matches Animal's now
            print "Biological Family: Canidae"
            print "Class Name: Dog"

    d = Dog()
    d.print_class_information()

References
----------
- Pylint - W0221
