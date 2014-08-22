Unused argument %r
^^^^^^^^^^^^^^^^^^

Description
-----------

An argument wich was defined in the header of a function or method is not used its body.

Example
-------

.. code:: python

    def my_function(arg_1, arg_2):
        arg_1 = arg_1 / 5 
        return arg_1

Even though :code:`arg_2` is defined as argument, it is not used in this function.

Solution(s)
-----------

- Remove the argument

.. code:: python

    def func(arg_1):
        arg_1 = arg_1 / 5 
        return arg_1

You can remove :code:`arg_2` to avoid this error. Be aware though that this might break your code. If :code:`func` is called with two arguments (e.g., :code:`func(10,3)`) this will raise an error. If you remove an argument, you have to refactor your code to make sure only one argument is passed.

- Delete the argument

.. code:: python

  def func(arg_1, arg_2):
      arg_1 = arg_1 / 5 
      del arg_2
      return arg_1
    
- Use :code:`*args` and :code:`**kwargs`

.. code:: python

  def func(arg_1, *args, **kwargs):
      arg_1 = arg_1 / 5 
      del arg_2
      return arg_1

If you are not sure whether :code:`arg_2` is passed to :code:`func` you can add :code:`*args` and :code:`*kwargs` to your function header. :code:`func(10,3)` can now be called without errors.

Alternatives
------------

- None

Further reading
---------------

References
---------------
- [PyLint W0613](http://pylint-messages.wikidot.com/messages:w0613)
