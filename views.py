from django import views
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
import markdown


class PageDetail(DetailView):
    model = Page
    template_name = 'ppclp/page_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['elements'] = context_data['page'].element_set.all()
        for el in context_data['elements']:
            el.content = markdown.markdown(el.content)
            for i in range(6,0,-1):
                for header_tag in ['<h', '</h']:
                    header_level = i + el.level + 1
                    if header_level > 6:
                        if header_tag == '<h':
                            el.content = el.content.replace(header_tag + str(i), '<h6 class="h' + str(header_level) + '"')
                        else:
                            el.content = el.content.replace(header_tag + str(i), '</h6')  
                    else:
                        el.content = el.content.replace(header_tag + str(i), header_tag + str(header_level))

        return context_data
        
