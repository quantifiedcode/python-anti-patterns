``TEMPLATE_DIRS`` deprecated
============================

This setting is deprecated since Django version 1.8. Set the ``DIRS`` option of a [`DjangoTemplates` backend](https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.template.backends.django) instead.

Deprecated feature
------------------

Deprecated ``TEMPLATE_DIRS`` setting used.

.. code:: python

    """ settings.py """

    TEMPLATE_DIRS = [
        "path/to/my/templates",
    ]

Migration path
--------------

As of Django 1.8 you should set ``DIRS`` option within ``TEMPLATES`` setting. It defines where the engine should look for template source files, in search order.

.. code:: python

    """ settings.py """

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'DIRS': '/path/to/my/templates',
        },
    ]


References
----------

- `Django documentation - Settings: TEMPLATES <https://docs.djangoproject.com/en/1.8/ref/settings/#templates>`_
- `Django documentation - Settings: TEMPLATE_DIRS <https://docs.djangoproject.com/en/1.8/ref/settings/#template-dirs>`_
- `Django documentation - Templates: Built-in backends <https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.template.backends.django>`_


Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/4af01dfd013241f58d0469e014209e3a>`_

