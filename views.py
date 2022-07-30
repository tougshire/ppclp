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
            lv = str(el.level)
            el.title = '<h' + lv + '>' + el.title + '</h' + lv + '>'
            el.content = '<div class="content-block">' + markdown.markdown(el.content) + '</div>'

            #Push down heading levels within the content so a heading within content is lower than the heading
            #of the element.  So if the elemnent is level 2, then title is enclosed in h2 tags, and the following code
            #converts h1 tags in the content to h3
            for i in range(6,0,-1):
                for header_tag in ['<h', '</h']:
                    header_level = i + el.level
                    if header_level > 6:
                        if header_tag == '<h':
                            el.content = el.content.replace(header_tag + str(i) + '>', '<h6 class="h' + str(header_level) + '">')
                        else:
                            el.content = el.content.replace(header_tag + str(i) + '>', '</h6>')  
                    else:
                        el.content = el.content.replace(header_tag + str(i) + '>', '</div>' + header_tag + str(header_level) + '><div class="content-block">')

        return context_data
        
