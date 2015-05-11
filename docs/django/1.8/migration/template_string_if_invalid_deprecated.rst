``TEMPLATE_STRING_IF_INVALID`` deprecated
=========================================

This setting sets the output that the template system should use for invalid (e.g. misspelled) variables. The default value is an empty string ``''``. This setting is deprecated since Django version 1.8. Set the `string_if_invalid` option in the `OPTIONS` of a `DjangoTemplates` backend instead.

Deprecated feature
------------------

Deprecated ``TEMPLATE_STRING_IF_INVALID`` setting used.

.. code:: python

    """ settings.py """

    TEMPLATE_STRING_IF_INVALID = 'Invalid variable'

Migration path
--------------

As of Django 1.8 you should set ``string_if_invalid`` option in the ``OPTIONS`` of a ``DjangoTemplates`` backend instead.

.. code:: python

    """ settings.py """

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'DIRS': '/path/to/my/templates',
            'OPTIONS': {
                 'string_if_invalid': 'Invalid varialbe!',
             }
        },
    ]

References
----------

- `Django documentation - Settings: TEMPLATES <https://docs.djangoproject.com/en/1.8/ref/settings/#templates>`_
- `Django documentation - Settings: TEMPLATE_STRING_IF_INVALID <https://docs.djangoproject.com/en/1.8/ref/settings/#template-string-if-invalid>`_
- `Django documentation - Templates: Built-in backends <https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.template.backends.django>`_
- `Django documentation - Templates: How invalid variables are handled <https://docs.djangoproject.com/en/1.8/ref/templates/api/#how-invalid-variables-are-handled>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/6f1b0d6580e04149983617cefa39d08c>`_
