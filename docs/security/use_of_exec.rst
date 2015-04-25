use of exec
===========

The ``exec`` statement enables you to dynamically execute arbitrary Python code which is stored in literal strings. Building a complex string of Python code and then passing that code to ``exec`` results in code that is hard to read and hard to test. Anytime the ``Use of exec`` error is encountered, you should go back to the code and check if there is a clearer, more direct way to accomplish the task.

Anti-pattern
------------

Program uses ``exec`` to execute arbitrary Python code
......................................................

The sample code below composes a literal string containing Python code and then passes that string to ``exec`` for execution. This is an indirect and confusing way to program in Python.

.. code:: python

    s = "print \"Hello, World!\""
    exec s


Best practice
-------------

Refactor the code to avoid ``exec``
...................................

In most scenarios, you can easily refactor the code to avoid the use of ``exec``. In the example below, the use of ``exec`` has been removed and replaced by a function.

.. code:: python

    def print_hello_world():
        print "Hello, World!"

    print_hello_world()

References
----------

- `PyLint - W0122 <http://pylint-messages.wikidot.com/messages:w0122>`_
- `Python Language Reference - The exec statement <https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement>`_
- `Stack Overflow - Why should exec() and eval() be avoided? <http://stackoverflow.com/questions/1933451/why-should-exec-and-eval-be-avoided>`_
