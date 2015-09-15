TEMPLATE_LOADERS deprecated
===========================

This setting is deprecated since Django version 1.8. Set the `LOADERS` option of a `DjangoTemplates backend <https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.templatebackends.django>`_ instead.

Deprecated feature
------------------

Deprecated ``TEMPLATE_LOADERS`` setting used.

.. code:: python

    """ settings.py """

    TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
    )


Migration path
--------------

As of Django 1.8 you should set ``loaders`` option in the ``TEMPLATES`` setting. It defines where the engine should look for template source files, in search order.

.. code:: python

    """ settings.py """

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'DIRS': '/path/to/my/templates',
            'OPTIONS': {
                 'loaders': (
                     'django.template.loaders.filesystem.Loader',
                     'django.template.loaders.app_directories.Loader',
                  ),
             }
        },
    ]


References
----------

- `Django documentation - Settings: TEMPLATES] <https://docs.djangoproject.com/en/1.8/ref/settings/#templates>`_
- `Django documentation - Settings: TEMPLATE_DIRS] <https://docs.djangoproject.com/en/1.8/ref/settings/#template-loaders>`_
- `Django documentation - Templates: Built-in backends] <https://docs.djangoproject.com/en/1.8/topics/templates/#module-django.template.backends.django>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/1f408fdeddad425192c87dc2b101fc51>`_

