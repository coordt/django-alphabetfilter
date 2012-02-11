"""
A generic view for filtering querysets via alphafilter
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
try:
    from django.views.generic import ListView
except ImportError:
    ListView = None

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

if ListView is not None:
    class AlphafilterListView(ListView):
        """
        Generic list view that filters the queryset by the choosen letter.
        The template name suffix for this views is _alfalist, so instead
        app/model_list.html, use app/model_alfalist.html.
        """
        template_name_suffix = '_alfalist'

        def get_queryset(self):
            queryset = super(AlphafilterListView, self).get_queryset()
            
            qs_filter = {}
            for key in self.request.GET.keys():
                if '__istartswith' in key:
                    qs_filter[str(key)] = self.request.GET[key]
                    break
            
            return queryset.filter(**qs_filter)
