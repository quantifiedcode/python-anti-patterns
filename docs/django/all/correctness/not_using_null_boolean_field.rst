Not using ``NullBooleanField``
==============================

A ``BooleanField`` in Django accepts only the two values: ``true`` and ``false``. If you need to accept ``NULL`` values, you have to use a ``NullBooleanField``.

Anti-pattern
------------

The following model uses a ``BooleanField`` with the option ``null=True``, instead of using a ``NullBooleanField``.

.. code:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        activated = models.BooleanField(null=True)


Best practice
-------------

Use a ``NullBooleanField`` instead:

.. code:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        # Using NullBooleanField instead
        activated = models.NullBooleanField()

Reference
---------

- [Django documentation - Model field reference: BooleanField (https://docs.djangoproject.com/en/1.8/ref/models/fields/#booleanfield)
- [Django documentation - Model field reference: NullBooleanField (https://docs.djangoproject.com/en/1.8/ref/models/fields/#nullbooleanfield)

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/f9a71a2aeef846ceafce68f5652b9dad>`_
