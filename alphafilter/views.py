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
        {'objects': queryset.filter(**qs_filter),
         'unfiltered_objects': queryset},
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
            # store queryset witouth filters so it can be used to generate
            # available letter list.
            self.unfiltered_queryset = queryset

            qs_filter = {}
            for key in self.request.GET.keys():
                if '__istartswith' in key:
                    qs_filter[str(key)] = self.request.GET[key]
                    break
            
            return queryset.filter(**qs_filter)

        def get_context_data(self, **kwargs):
            """
            Add 'unfiltered_queryset' variable to context with the original
            queryset, before limiting to the selected letter.
            """
            context = super(AlphafilterListView, self).get_context_data(**kwargs)
            context['unfiltered_queryset'] = self.unfiltered_queryset
            return context
