===================================
The qs_alphabet_filter Template Tag
===================================

If you wanted to have an alphabet filter in a regular template, the ``qs_alphabet_filter`` template tag will generate this for you.

Requirements
============

Make sure that Django's ``TEMPLATE_CONTEXT_PROCESSORS`` setting in your ``settings.py`` includes ``django.core.context_processors.request``, which is not included by default.

.. code-block:: python

	TEMPLATE_CONTEXT_PROCESSORS = (
	    "django.core.context_processors.auth",
	    "django.core.context_processors.debug",
	    "django.core.context_processors.i18n",
	    "django.core.context_processors.media",
	    "django.core.context_processors.request",
	)

Without this context processor, the template tag will have no idea which letter was clicked on and can't display the currently selected letter.

Usage
=====

Within your template, load the template tag library and use the ``qs_alphabet_filter`` tag, with at least two parameters: the variable containing the QuerySet and the name (or variable containing the name) of the field to apply the alphabet filter.

.. code-block:: django

	{% load alphafilter %}
	{% qs_alphabet_filter objects last_name %}

With two parameters, the default template ``alphafilter/alphabet.html`` is used to render the selection. You may pass a third parameter for your own template (but you can simply override the default).

There are three other things that you may need: the alphabet filter template, CSS styles, and a view that returns a filtered QuerySet to display the results. 

Alphabet Filter Template
************************

The template tag allows you to specify the template that is specifically rendered, but the default is ``alphafilter/alphabet.html`` and should fit most needs.

For those of you who are more adventurous, the context of the template includes:

choices
	A list of dictionaries containing all the choices to display. This will include all letters of the ``DEFAULT_ALPHABET`` setting as well as additional letters contained within the data, and an item to display all of the items.
	
	This list is sorted with the "All" item first, and the other items sorted in alphabetical order.


Each list item dictionary contains:
	
has_entries
	True if the letter has entries in the data set.

link
	The HTML link for the choice, typically rendered as the ``href`` of an ``<a>`` tag. For example: ``<a href="{{ choice.link }}">``

title
	The name of the letter, or (localizable) "All"

active
	This letter is currently selected.

The default template looks something like:

.. code-block:: django

	{% if choices %}
	    <ul class="alphabetfilter">
	    {% for choice in choices %}
	        <li>{% if choice.has_entries %}
	            <a href="{{ choice.link }}">
	        {% else %}
	            <span class="inactive">
	        {% endif %}
	        {% if choice.active %}
	            <span class="selected">
	        {% endif %}
	        {{ choice.title }}
	        {% if choice.active %}
	            </span>
	        {% endif %}
	        {% if choice.has_entries %}
	            </a>
	        {% else %}
	            </span>
	        {% endif %}
	        </li>
	    {% endfor %}
	    </ul>
	    <br class="clear" />
	{% endif %}


CSS Styles
**********

For convenience, a template is included for some basic CSS styling, simply include ``alphafilter/alphafilter_styles.html`` in the appropriate place in your template:

.. code-block:: html

	<head>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	    <title>AlphaFilter Test</title>
	    
	    {% include "alphafilter/alphafilter_styles.html" %}
	    
	</head>

You can also override the template in your project by simply creating a file called ``alphafilter_styles.html`` within a directory named ``alphafilter`` inside your projects templates directory.

The default styles are:

.. code-block:: css

	<style type="text/css" media="screen">
	ul.alphabetfilter {
	    list-style: none;
	    display: inline;
	}
	ul.alphabetfilter li {
	    width: 0.7em;
	    display: inline;
	}
	.inactive {
	    color: #999;
	}
	.selected {
	    color: red;
	}
	</style>


The View
********

Django AlphaFilter includes a generic view named ``alphafilter.views.alphafilter`` that is useful as an example, but might not be very useful for all situations.

The view needs to do two things: look for the filter in ``request.GET``\ and add a filtered QuerySet in the context for rendering the template. The template can then iterate through the QuerySet to display the results.

The example view accepts an HttpRequest, a QuerySet, and a template name. It finds the filter by looking for a key in the GET parameters containing '__istartswith', and uses that to filter the QuerySet. The filtered QuerySet is passed into the context as 'objects'.

.. code-block:: python

	def alphafilter(request, queryset, template):
	    qs_filter = {}
	    for key in request.GET.keys():
	        if '__istartswith' in key:
	            qs_filter[str(key)] = request.GET[key]
	            break
	    
	    return render_to_response(
	        template, 
	        {'objects': queryset.filter(**qs_filter)}, 
	        context_instance=RequestContext(request)
	    )

