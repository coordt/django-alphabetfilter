"""
A generic view for filtering querysets via alphafilter
"""
from django.shortcuts import render_to_response
from django.template import RequestContext

def alphafilter(request, queryset, template):
    """
    Render the template with the filtered queryset
    """
    
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