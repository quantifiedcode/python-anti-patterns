Not using forward slashes
=========================

Django requires you to use forward slashes ``/`` whenever you indicate a path, even on Windows. In your settings, this is true for the following variables.

- ``STATICFILES_DIRS``
- ``TEMPLATE_DIRS``
- ``DATABASES['<your database>'][NAME]``
- ``FIXTURE_DIRS``

Anti-pattern
------------

This pattern is exemplary for any of the above mentioned settings. It uses backslashes, instead of forward slashes.

.. code:: python

    """ settings.py """

    STATICFILES_DIRS = [
        "\path\to\my\static\files",
    ]

Best practice
-------------

Django requires you to use forward slashes ``/``, even on Windows.

.. code:: python

    """ settings.py """

    STATICFILES_DIRS = [
        "\path\to\my\static\files",
    ]

References
----------

- `Django documentation - Settings: TEMPLATE_DIRS <https://docs.djangoproject.com/en/1.8/ref/settings/#template-dirs>`_
- `Django documentation - Settings: FIXTURE_DIRS <https://docs.djangoproject.com/en/1.8/ref/settings/#fixture-dirs>`_
- `Django documentation - Settings: STATIC_FILES_DIRS <https://docs.djangoproject.com/en/1.8/ref/settings/#https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-dirs>`_
- `Django documentation - Settings: HOST <https://docs.djangoproject.com/en/1.8/ref/settings/#host>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/ff48f625efa5424088acfc1ea788db3e>`_
