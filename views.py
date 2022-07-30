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
        for element in context_data['elements']:
            element_level_str = str(element.level)
            element.title = '<h' + element_level_str + '>' + element.title + '</h' + element_level_str + '>'
            element.content = '<div class="content-block">' + markdown.markdown(element.content) + '</div>'

            #Push down heading levels within the content so a heading within content is lower than the heading
            #of the element.  So if the elemnent is level 2, then title is enclosed in h2 tags, and the following code
            #converts h1 tags in the content to h3
            for i in range(6,0,-1):
                for header_tag in ['<h', '</h']:

                    header_level = i + element.level
                    header_level_str = str(header_level)
                    i_str = str(i)

                    if header_level > 6:
                        if header_tag == '<h':
                            element.content = element.content.replace(header_tag + i_str + '>', '</div><h6 class="h' + header_level_str + '">')
                        else:
                            element.content = element.content.replace(header_tag + i_str + '>', '</h6><div class="content-block">')  
                    else:
                        if header_tag == '<h':
                            element.content = element.content.replace(header_tag + i_str + '>', '</div>' + header_tag + header_level_str + '>')
                        else:
                            element.content = element.content.replace(header_tag + i_str + '>', header_tag + header_level_str + '><div class="content-block">')

        return context_data
        
