``ALLOWED_HOSTS`` setting missing
=================================

In Django, you need to properly set the ``ALLOWED_HOSTS`` setting when ``DEBUG = False``. This is a security mechanism. It prevents attackers from poisoning caches or password reset emails with links to malicious hosts by submitting requests with a fake HTTP Host header, which is possible even under many seemingly-safe web server configurations.

Anti-Pattern
------------

``ALLOWED_HOSTS`` not set or empty, when ``DEBUG = False``.

... code:: python
    """ settings.py """

    DEBUG = False
    # ...
    ALLOWED_HOSTS = []

Best practice
-------------

Make sure, an appropriate host is set in `ALLOWED_HOSTS`, whenever `DEBUG = False`.

... code:: python
    DEBUG = False
    # ...
    ALLOWED_HOSTS = ['djangoproject.com']

References
----------

- `Django documentation - Settings: The Basics` <https://docs.djangoproject.com/en/1.8/topics/settings/#the-basics>`_
- `Django documentation - Settings: ALLOWED_HOSTS` <https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ALLOWED_HOSTS>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/1686e34613394079976afdd3e9a9d5d8?tab=meta>`_
