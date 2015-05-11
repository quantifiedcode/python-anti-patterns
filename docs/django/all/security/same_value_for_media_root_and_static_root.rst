Same value for MEDIA_ROOT and STATIC_ROOT
=========================================

According to Django's documentation, ``MEDIA_ROOT`` and ``STATIC_ROOT`` must have different values. Before STATIC_ROOT was introduced, ``MEDIA_ROOT`` was also used (as fallback) to also serve static files. As this can have serious security implications, Django has validation checks to prevent it.

Anti-pattern
------------

``MEDIA_ROOT`` and ``STATIC_ROOT`` point to the same folder.

.. code:: python

    """ settings.py """

    # Media and static root are identical
    STATIC_ROOT = '/path/to/my/static/files'
    MEDIA_ROOT = '/path/to/my/static/files'

Best practice
-------------

Ensure, ``STATIC_ROOT`` and ``MEDIA_ROOT`` point to different folders.

.. code:: python
    
    """ settings.py """

    STATIC_ROOT = '/path/to/my/static/files'
    MEDIA_ROOT = '/path/to/my/media/files'

References
----------

- `Django documentation - Settings: MEDIA_ROOT <https://docs.djangoproject.com/en/1.8/ref/settings/#media-root>`_

Status
------

- `Automated code check available <https://www.quantifiedcode.com/app/pattern/617b8feb087f4a5fafa2934d78ace2a8>`_
