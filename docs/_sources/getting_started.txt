
===============
Getting Started
===============

There are two ways to incorporate the alphabet filter into your project and applications. The first is modifying one or more application's ``ModelAdmin`` classes. The second is when you don't have control of the code and want to add the feature, such as to ``django.contrib.auth``\ . Both methods require you to override the default admin template for that model or app.


Overriding the Admin Template
=============================

In order to properly display the alphabet filter in the admin, the ``change_list.html`` template must be slightly changed. ``django-alphafilter`` includes a template the makes the proper changes. This template extends the default admin template, so using it must be done on an per-application or per-model basis.

You can merge the default Django admin ``change_list.html`` template with ``django-alphafilter``\ 's changes to make a single template override. ``django-alphafilter`` doesn't do this so it can support multiple Django versions.

Within your project's template directory, you need to create an ``admin`` directory, and a directory with the name of the application, and optionally the name of the model. For example, if you were adding the filter on the ``Tag`` model of an application named ``cooltags``\ , the directory structure would look like::


	MyProject
	    templates
	        admin
	            cooltags
	                change_list.html      <-- For every model in the cooltags
	                tag
	                    change_list.html  <-- For just the Tag model


The ``change_list.html`` file simply needs to contain the line::

	{% extends "alphafilter/change_list.html" %}

.. note:: You **cannot** place this template in the ``admin`` directory, as it leads to an infinite loop of inheritance. As mentioned above, you can create a new ``change_list.html`` template by copying the ``django.contrib.auth`` template and make the same adjustments as the ``django-alphafilter``\ 's template.


Altering Your Own Model Admin
=============================

If you have control of the application's code, you can easily support ``django-alphafilter`` by adding an ``alphabet_filter`` attribute to your ``ModelAdmin`` class, like so::

	class TestNameAdmin(admin.ModelAdmin):
	    model = TestName
	    alphabet_filter = 'sorted_name'

The value of ``alphabet_filter`` is the name of the field to use for filtering.


Altering Another Application's Model Admin
==========================================

Sometimes you want to use the alphabet filter, but you don't want to modify someone else's code. A perfect example is ``django.contrib.auth``\ . To enable the alphabet filter on the ``User`` model, you can add a configuration setting in your ``settings.py``\ . The ``ALPHAFILTER_ADMIN_FIELDS`` setting is a dictionary in the form of ``{'<appname>.<modelname>': '<fieldname>', [ ... ] }``

For example::

	ALPHAFILTER_ADMIN_FIELDS = {
	    'auth.user': 'username',
	    'auth.group': 'name',
	}

