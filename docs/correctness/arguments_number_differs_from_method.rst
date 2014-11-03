Arguments number differs from method
====================================

Summary
-------

A child class has implemented an abstract method with a different number of arguments than what is defined in the method signature of the parent class. Treat this error as a warning. The child class' implementation should match the argument signature defined in the parent class.

Description
-----------

There are two outcomes that can occur when the number of arguments in a child class implementation does not match the abstract method signature in the parent class. If the child class contains more arguments than the parent class, then Python can execute the code. If the number of arguments in the child class is less than the parent class abstract method signature, then Python cannot execute the code. Either way, this defeats the purpose of abstract methods. Abstract methods are contracts passed down to inherited classes from parent classes. The children are supposed to implement a method that matches the argument signature defined by the parent. When the child class does not match the signature defined in the parent class, it is not fulfilling its part of the inheritance contract.

Examples
----------

Child class method contains more arguments than parent class method signature
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
