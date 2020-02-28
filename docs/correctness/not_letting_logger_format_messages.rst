Not letting logger format messages
----------------------------------

When you log a message, do not format your message with parameters. You should
let logger lib handle that.


Anti-pattern
------------

.. code:: python
    msg = "Error %s catched!"
    logger.error(msg % 1337)


Best practice(s)
----------------

Let logger format message
.........................

Pass message parameters as arguments to the logger function.

.. code:: python
    msg = "Error %s catched!"
    logger.error(msg,  1337)


References
----------
- `Python logging howto <https://docs.python.org/3/howto/logging.html#logging-variable-data>`_
