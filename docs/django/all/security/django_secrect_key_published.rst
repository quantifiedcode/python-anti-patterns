SECRET_KEY published
====================

A secret key has to be be kept secret. Make sure it is only used in production, but nowhere else. Especially, avoid committing it to source control. This increases security and makes it less likely that an attacker may acquire the key.

Anti-pattern
------------

This settings.py contains a SECRET_KEY. You should not do this!

.. code:: python

    """ settings.py """
    SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

Best Practices
--------------
Load key from environment variable
..................................

Instead of publishing your secret key, you can use an environment variable to set your secret key.

.. code:: python

    import os
    SECRET_KEY = os.environ['SECRET_KEY']


Load secret key from file
.........................

Alternatively, you can read the secret key from a file.

.. code:: python

    with open('/etc/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()

References
-----------
- `Django <https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/>`_


Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/3fc074e3040b459fb393d170adf47d33>`_
