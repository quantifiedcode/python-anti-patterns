Using NullBooleanField
==========================

To make a boolean field that accepts ``NULL`` values in addition to ``true`` and ``false``, use a ``BooleanField`` with the option ``null=True``, rather than a ``NullBooleanField``.

The ``null=True`` option for ``BooleanField`` was introduced in Django 2.1. ``NullBooleanField`` was deprecated in Django 3.1, and is removed in Django 4.0.

Anti-pattern
-------------

The following model uses a ``NullBooleanField``.

.. code:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        activated = models.NullBooleanField()

Best practice
--------------

Instead, use a ``BooleanField`` with the option ``null=True``.

.. code:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        activated = models.BooleanField(null=True)

Reference
---------

- `Django documentation - Model field reference: BooleanField <https://docs.djangoproject.com/en/3.1/ref/models/fields/#booleanfield>`_
- `Django documentation - Model field reference: NullBooleanField <https://docs.djangoproject.com/en/3.1/ref/models/fields/#nullbooleanfield>`_
