Unused argument %r
^^^^^^^^^^^^^^^^^^

Description
-----------

An argument is not used in the body of the respective function or method.

Example
-------

.. code:: python

    def my_function(arg_1, arg_2):
        arg_1 = arg_1 / 5 
        return arg_1

Even though arg_2 is defined as argument, it is not used in this function. This is problematic because ...

Solution(s)
-----------

- Remove the argument

.. code:: python

    def func(arg_1):
        arg_1 = arg_1 / 5 
        return arg_1

You can remove arg_2 to avoid this error. Be aware though that this might break your code. If `func` is called with two arguments (e.g., `func(10,3)`) this will raise an error. If you remove an argument, you have to refactor your code to make sure only one argument is passed.

- Delete the argument

.. code:: python

  def func(arg_1, arg_2):
      arg_1 = arg_1 / 5 
      del arg_2
      return arg_1
    
- Use *args and **kwargs

.. code:: python

  def func(arg_1, *args, **kwargs):
      arg_1 = arg_1 / 5 
      del arg_2
      return arg_1

If you are not sure whether arg_2 is passed to `func` you can add  `*args` and `**kwargs` to your function header. Like this, `func(10,3)` can still be called without causing an error.

Alternatives
------------


Further reading
---------------

PyLint reference
---------------
- 
