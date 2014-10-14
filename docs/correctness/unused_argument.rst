Unused argument
===============

Description
===========

An argument of a function or method is not used in its body. This error is not critical, but considered bad style.

Examples
==========

The following function header defines two arguments :code:`arg_1` and :code:`arg_2`. Even though :code:`arg_2` is defined, it is not used in the function's body.

.. code:: python

    def func(arg_1, arg_2):
        arg_1 = arg_1 / 5 
        return arg_1

Solutions
===========

- Remove the argument

    You can remove :code:`arg_2` from the header of your function / method. 
    
    .. code:: python

        def func(arg_1):
            arg_1 = arg_1 / 5 
            return arg_1

        def run():
            func(10,3) # raises exception
            
    .. caution:: 
        Be aware that this might break your code elsewhere. If :code:`func` is called with two arguments (e.g., :code:`func(10,3)`) this will raise an error. If you remove an argument, you have to refactor your code to make sure only one argument is passed.

- Delete the argument

    .. code:: python

        def func(arg_1, arg_2):
            arg_1 = arg_1 / 5 
            del arg_2 # delete arg_2
            return arg_1
      
        def run():
            func(10,3) # executes without error
    
- Use :code:`*args` and :code:`**kwargs`

    If you are not sure whether :code:`arg_2` is passed to :code:`func` you can add :code:`*args` and :code:`*kwargs` to your function header. :code:`func(10,3)` can now be called without errors.

    .. code:: python

        def func(arg_1, *args, **kwargs): #add *args and **kwargs
            arg_1 = arg_1 / 5 
            return arg_1
      
        def run():
            func(10,3) # executes without error
            func(10, arg_2=4) # executes without error

References
==========
- `PyLint W0613 <http://pylint-messages.wikidot.com/messages:w0613>`_
