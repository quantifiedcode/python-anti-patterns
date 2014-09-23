An attribute hides this method
==============================

Summary
-------

An attribute and a method of a class share the same name. Give the two objects unique names or else Python will raise a ``TypeError: object is not callable`` error at runtime. Python raises the error because the name is associated to the attribute, so when you insert parentheses after the name, Python actually tries to call the attribute although you were trying to call the function.

Description
-----------

When an attribute and a method have the same name, Python gives the attribute precedence. Because two objects cannot have the same name while residing in the same namespace, the method will effectively be hidden. If you try to call the method, Python will actually attempt to call the attribute, and a ``TypeError`` runtime error will occur and the module will not successfully execute. Therefore when you encounter this error you must modify the attribute and method to have unique names.

This error often occurs when somebody implements a getter/setter method for accessing an instance attribute. Python style conventions actually prefers that you remove the getter/setter method and just access the attribute directly.

Examples
----------

Attribute and method have the same name
.......................................

In the module below, the author defines a class named ``Rectangle``. The class includes an attribute named ``area`` and a method for getting or setting that attribute. Because the names are the same, the attribute hides the method. When the module attempts to call the ``area`` method Python raises a ``TypeError: object is not callable`` and the module does not successfully execute.

.. warning:: The code below is an example of an error. Using this code will create bugs in your programs!

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        def area(self, value=None):  # hidden because of attribute with same name
            if value == None:
                return self.area
            else:
                self.area = value

    r = Rectangle(3, 4)
    print r.area()  # TypeError: int is not callable

Solutions
---------

Modify the names
................

Per Python style conventions, the author modified his ``Rectangle`` class by deleting the ``area`` method. Whenever a module needs to access the ``area`` attribute of a ``Rectangle`` instance, the module can just access the ``area`` attribute directly. This also suppresses the ``Attribute hides this method`` error.

.. code:: python

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
        # deleted area method from here

    r = Rectangle(3, 4)
    print r.area  # access the attribute directly now
    
References
----------
- `PyLint - E0202 <http://pylint-messages.wikidot.com/messages:e0202>`_
- `Stack Overflow - Getter/Setter Methods <http://stackoverflow.com/questions/8297723/oop-getter-setter-methods>`_
