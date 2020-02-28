Inefficient database queries
============================

Django's models make it easy for you, to filter the data of your application without using any SQL statements. This is a great thing, however, it sometimes hides that you are using object filters inefficiently. Unless you append ``.values()`` to your filter, your QuerySet will always query all columns within your database. This can be uncritical until you scale your application or once your tables grow bigger. Therefore, make sure you only retrieve the columns your really need within your program.

Anti-Pattern
------------

Let's assume we have a an app ``vehicle`` which contains a model ``Cars`` to store plenty of information about a car:

.. code:: python

    """ models.py """

    class Cars(models.Model):
        make = models.CharField(max_length=50)
        model = models.CharField(max_length=50)
        wheels = models.CharField(max_length=2)
        # ...


We import this model into one of your views to do something will make names within our database:

.. code:: python

    """ views.py """
    from models import Cars

    # ...

    cars = Cars.objects.all()
    for car in cars:
        do_something(car.make)


Even though this code works and looks harmless, it can kill you in production. You think, you are actually just accessing the ``make`` field, but you are actually retrieving ALL data from your database, once you start iterating over the retrieved QuerySet:

.. code:: sql

    SELECT make, model, wheels, ... FROM vehicles_cars;

Especially, if you have many fields on your model and/or if you got millions of records in your table, this slows down the response time of your applications significantly. As QuerySets are cached upon evaluation, it will hit your database only once, but you'd better be carful.

Best practice
-------------

Use ``.values()``
.................

To avoid such scenario, make sure you only query the data you really need. Use ``.values()`` to restrict the underlying SQL query to required fields only.

.. code:: python

    """ views.py """
    from cars.models import Cars

    cars = Cars.objects.all().values('make')

    # Print all makes
    for car in cars:
        do_something(car['make'])

.. code:: sql

    SELECT make from vehicles_cars;

Use ``.values_list()``
......................

Alternatively, you can use ``.value_list()``. It is similar to ``values()`` except that instead of returning dictionaries, it returns tuples when you iterate over it.

.. code:: python

    """ views.py """
    from cars.models import Cars

    cars = Cars.objects.all().values_list('make', flat=True)

    # Print all makes
    for make in cars:
        do_something(make)


References
----------

- `Django documentation - Models: Querysets (values) <https://docs.djangoproject.com/en/1.8/ref/models/querysets/#values>`_
- `Django documentation - Models: Querysets (values_list) <https://docs.djangoproject.com/en/1.8/ref/models/querysets/#values_list>`_



