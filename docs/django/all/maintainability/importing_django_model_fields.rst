Importing ``django.db.models.fields``
=====================================

In Django, models are defined in ``django.db.models.fields``. However, for convenience they are imported into ``django.db.models``. Django's standard convention is to use ``from django.db import models`` and refer to fields as ``models<some>Field``. To improve readability and maintainability of your code, change your import statement and model definition.

Anti-pattern
------------

... code:: python

    from django.db.models import fields

    class Person(models.Model):
        first_name = fields.CharField(max_length=30)
        last_name = fields.CharField(max_length=30)

Best practice
-------------

Stick to standard conventions and use ``from django.db import models`` instead.

... code:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

References
----------

- `Django documentation - Model field reference <https://docs.djangoproject.com/en/1.8/ref/models/fields/#module-django.db.models.fields>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/cde20ce818b44fbf9d17176f03922be3>`_
