Not using variable name for optional arguments
==============================================

Non-optional arguments must be added before optional arguments and will disrupt existing calls to the method if the programmer failed to name all optional arguments used. Also there is no guarentee that the order of the optional arguments might not change in the future. Always naming optional arguments used also improves the readability and maintainability of the code.


Anti-pattern
------------

The code below does not name the optional arguments used when calling the foo method. This results in unexpected behavior when the bar argument is added to the foo method by another developer but who fails to account for all callers of the method.

.. code:: python
    from __future__ import print_function

    def foo(message, bar, count=0):
        print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", 10)


Even if bar is added as an optional argument it might be added before count and results in unexpected behavior as shown in the code below:

.. code:: python
    from __future__ import print_function

    def foo(message, bar=None, count=0):
        if bar:
            print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", 10)


Best practice(s)
----------------

Always name optional arguments used when calling a method
.........................................................

The modified code below is the safest way to call the foo method. By always naming the optional arguments used you make it easier to detect callers that need to be fixed when adding non-optional arguments to the method in the future.

.. code:: python
    from __future__ import print_function

    def foo(message, bar, count=0):
        print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", count=10)


The above code will raise an error alerting the programmer to add the missing required bar argument. Whereas the addition of optional argument bar in the code below shows that no changes would be needed since the optional argument was named.

.. code:: python
    from __future__ import print_function

    def foo(message, bar=None, count=0):
        if bar:
            print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", count=10)
    foo("message", bar=80, count=10)


Always add new optional arguments to the end of a method
........................................................

Adding new optional arguments to the end of a method also ensures that the callers behave as expected as shown in the code below:

.. code:: python
    from __future__ import print_function

    def foo(message, count=0, bar=None):
        if bar:
            print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", 10)
    foo("message", 10, 80)


The code above demonstrates how always adding optional arguments to the end prevents unexpected behavior but also demonstrates how unreadable the methods becomes as more optional arguments are added as compared to the code below:

.. code:: python
    from __future__ import print_function

    def foo(message, count=0, bar=None):
        if bar:
            print("=" * bar)
        for i in range(count):
            print(message)

    foo("message", count=10)
    foo("message", count=10, bar=80)


