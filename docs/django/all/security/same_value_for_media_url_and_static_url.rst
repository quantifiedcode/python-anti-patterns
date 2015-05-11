Same value for MEDIA_URL and STATIC_URL
=======================================

According to Django's documentation, ``MEDIA_URL`` and ``STATIC_URL`` must have different values.

Anti-pattern
------------

``MEDIA_URL`` and ``STATIC_URL`` point to the same folder.

.. code:: python

    """ settings.py """

    # Media and static root are identical
    STATIC_URL = 'http://www.mysite.com/static'
    MEDIA_URL = 'http://www.mysite.com/media'

Best practice
-------------

Ensure, `STATIC_URL` and `MEDIA_URL` point to different folders.

.. code:: python

    """ settings.py """

    STATIC_ROOT = '/path/to/my/static/files'
    MEDIA_ROOT = '/path/to/my/media/files'

References
----------

- `Django documentation - Settings: MEDIA_URL <https://docs.djangoproject.com/en/1.8/ref/settings/#media-url>`_
- `Django documentation - Settings: MEDIA_ROOT <https://docs.djangoproject.com/en/1.8/ref/settings/#media-root>`_


Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/6ea0427fc8c043bf9d4c1ad3ebf18add>`_
