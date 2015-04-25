Using single letter to name your variables
==========================================

Sometimes you see programmers trying to shorten the ammount of text needed to write a piece of code, but when this goes to exremes, it will result in extremely ugly and unreadable code.

Anti-pattern
------------

.. code:: python

    d = {'data': [{'a': 'b'}, {'b': 'c'}, {'c': 'd'}], 'texts': ['a', 'b', 'c']}

    for k, v in d.iteritems():
        if k == 'data':
            for i in v:
                # Do you know what are you iterating now?
                for k2, v2 in i.iteritems():
                    print k2, v2


Best practice
-------------

Use more verbose name for your variables for clarity
....................................................

It is much better to write more text, but be much more precise what each variable means.

.. code:: python

    data_dict = {
        'data': [{'a': 'b'}, {'b': 'c'}, {'c': 'd'}],
        'texts': ['a', 'b', 'c']
    }

    for key, value in data_dict.iteritems():
        if key == 'data':
            for data_item in value:
                # Do you know what are you iterating now?
                for data_key, data_value in data_item.iteritems():
                    print data_key, data_value
