==================
Django AlphaFilter
==================

Django AlphaFilter was designed to work like Django's default ``date_hierarchy`` admin filter. It puts an clickable alphabet in the same location as the date hierarchy - at the top of the results list.

**Changes in 0.7:**

* Django 1.5 compatible.

* Fall back to previous method of retrieving letters in Django 1.4, due to bug in Django's aggregation.

* Fixed the encoding of "&" in the urls.

* Added ``unfiltered_queryset`` to the context (Thanks to Ales Zabala Alava: https://github.com/shagi)

**Changes in 0.6:**

* Switched to Django querysets to retrieve letters. (Thanks to Ales Zabala Alava: https://github.com/shagi)

* Django 1.4 compatible

**Changes in 0.5:**

* Added a new template tag to render the alphabet filter in a normal template using a queryset and field and optionally specified template.

**Changes in 0.4:**

* Added the ability to specify a 3rd-party application to apply the alphabet filter without having to modify that code (e.g. ``django.contrib.auth``\ ). The ``ALPHAFILTER_ADMIN_FIELDS`` setting is used for this.

* Now includes documentation!

**Changes in 0.3:**

* The ``ModelAdmin`` class can now specify its own ``DEFAULT_ALPHABET`` to use instead of the global setting.

* ``DEFAULT_ALPHABET`` can now be a callable


Installation
============

1. The easiest method is to use ``pip``\ ::

	pip install django-alphafilter

2. If you download the source, you can install it by running the ``setup.py`` script::

	cd /path/to/django-alphafilter/
	python setup.py install

3. Add ``'alphafilter'`` to your project's ``settings.py`` file, so Django will find the templates and template tag.

Default Alphabet
================

The default alphabet is the list of characters displayed in the admin even if there is no data for that character. As there is data, the letters of the alphabet are enabled. Any characters not in the default alphabet, but that exist in the data, are added dynamically.

Due to issues regarding devising the proper alphabet by language, the default alphabet is a setting named ``DEFAULT_ALPHABET``\ . The default setting is the ASCII alphabet and digits. You can set the ``DEFAULT_ALPHABET`` to a string, list, tuple or callable.

If you only what the ASCII characters, no digits::

	DEFAULT_ALPHABET = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

For the German alphabet::

	DEFAULT_ALPHABET = u'0123456789A\xc4BCDEFGHIJKLMNO\xd6PQRS\xdfTU\xdcVWXYZ'

For the Icelandic alphabet::

	DEFAULT_ALPHABET = u'0123456789A\xc1BD\xd0E\xc9FGHI\xcdJKLMNO\xd3PRSTU\xdaVXY\xdd\xde\xd6'

You can override the ``DEFAULT_ALPHABET`` on a model-by-model basis by adding a ``DEFAULT_ALPHABET`` attribute to your ``ModelAdmin`` class like so::

	class TestNameAdmin(admin.ModelAdmin):
	    model = TestName
	    alphabet_filter = 'sorted_name'

	    # A blank string only shows the characters in the database
	    DEFAULT_ALPHABET = u''



The ordering of the alphabet will not stay the same as entered, it is sorted through Python's list sort method.

Using Alphabet Filter on a Model
================================

In the model's ``admin.py`` set ``alphabet_filter`` to the name of a character field. For example::

	alphabet_filter = 'name'

You also have to create a template for the model (or application) that will override the admin's ``change_list.html`` template.

Within your project's template directory, you need to create an ``admin`` directory, and a directory with the name of the application, and optionally the name of the model. For example, if you were adding the filter on the ``Tag`` model of an application named ``cooltags``\ , the directory structure would look like::

	MyProject
	    templates
	        admin
	            cooltags
	                tag

Create a document named ``change_list.html`` and put it in either the application (``templates/admin/cooltags``\ ) directory, to have it work for every model within that application or put it in the model directory (``templates/admin/cooltags/tag``\ ) to have it work only for that model.

The change_list.html document should only contain one line::

	{% extends "alphafilter/change_list.html" %}

.. note:: You **cannot** place this template in the ``admin`` directory, as it leads to an infinite loop of inheritance.