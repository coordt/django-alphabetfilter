========
Settings
========

DEFAULT_ALPHABET
================

This setting is used to display characters in the admin interface no matter what the data may contain. Characters are always displayed if they are in the data, but not in the ``DEFAULT_ALPHABET``\ .

The ``DEFAULT_ALPHABET`` can be a ``string``\ , ``list`` of ``string``\ s, a ``tuple`` of ``string``\ s, or a callable (a function or class instance with a ``__call__`` method) that returns one of the previous types.

``DEFAULT_ALPHABET`` defaults to the ``string.ascii_uppercase`` + ``string.digits``. Globally change this value by setting it in your ``settings.py`` file, or change it on a single model by setting it in the model's ``ModelAdmin``\ .


ALPHAFILTER_ADMIN_FIELDS
========================

The ``ALPHAFILTER_ADMIN_FIELDS`` setting is a dictionary in the form of ``{'<appname>.<modelname>': '<fieldname>', [ ... ] }``

For example::

	ALPHAFILTER_ADMIN_FIELDS = {
	    'auth.user': 'username',
	    'auth.group': 'name',
	}

