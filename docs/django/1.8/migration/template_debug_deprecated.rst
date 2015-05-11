``TEMPLATE_DEBUG`` deprecated
=============================

This setting sets the output that the template system should use for invalid (e.g. misspelled) variables. The default value is an empty string ``''``. This setting is deprecated since Django version 1.8. Set the `TEMPLATE_DEBUG` option in the ``OPTIONS`` of a ``DjangoTemplates`` backend instead.

Deprecated feature
------------------

Deprecated ``TEMPLATE_DEBUG`` setting used.

.. code:: python

    """ settings.py """

    TEMPLATE_DEBUG = True


Migration path
--------------

As of Django 1.8 you should set ``debug`` option in the ``OPTIONS`` of a ``DjangoTemplates`` backend instead.

.. code:: python

    """ settings.py """

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'DIRS': '/path/to/my/templates',
            'OPTIONS': {
                 'debug': True,
             }
        },
    ]

References
----------

- `Django documentation - Settings: TEMPLATE_DEBUG <https://docs.djangoproject.com/en/1.8/ref/settings/#template-debug>`_
- `Django documentation - Settings: TEMPLATES <https://docs.djangoproject.com/en/1.8/ref/settings/#templates>`_
- `Django documentation - Templates: Built-in backends <https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.template.backends.django>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/705f569e1a174f39946454933994e4b3>`_
