from concurrent.futures import process
from django import views
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Element, Page, Placement
import markdown


class PageDisplay(DetailView):
    model = Page
    template_name = 'ppclp/page_display.html'

    def process_content(self, placement):
        content = '<div class="content-block">' + markdown.markdown(placement.element.content) + '</div>'

        #Push down heading levels within the content so a heading within content is lower than the heading
        #of the element.  So if the elemnent is level 2, then title is enclosed in h2 tags, and the following code
        #converts h1 tags in the content to h3
        for i in range(6,0,-1):
            for header_tag in ['<h', '</h']:

                header_level = i + placement.level
                header_level_str = str(header_level)
                i_str = str(i)

                if header_level > 6:
                    if header_tag == '<h':
                        content = content.replace(header_tag + i_str + '>', '</div><h6 class="h' + header_level_str + '">')
                    else:
                        content = content.replace(header_tag + i_str + '>', '</h6><div class="content-block">')  
                else:
                    if header_tag == '<h':
                        content = content.replace(header_tag + i_str + '>', '</div>' + header_tag + header_level_str + '>')
                    else:
                        content = content.replace(header_tag + i_str + '>', header_tag + header_level_str + '><div class="content-block">')

        subplacements = placement.page.placement_set.filter(order__gt=placement.order)
        if subplacements.exists():
             if subplacements.first().level == placement.level + 1:
                stop=False
                for subplacement in subplacements:
                    if subplacement.level <= placement.level:
                        break
                    if subplacement.level == placement.level + 1:
                        sp_level = str(subplacement.level)
                        content = '<h' + sp_level + '>' + subplacement.element.title + '</h' + sp_level + '>'
                        content = content + self.process_content(subplacement)

        return content


    def get_context_data(self, **kwargs):
        print('tp 2281b15', 'self=', self)
        print('tp 2281b16', 'self.kwargs=', self.kwargs)
        print('tp 2281b17', 'kwargs=', kwargs)
        
        context_data = super().get_context_data(**kwargs)
        context_data['placements'] = self.object.placement_set.all()
        context_data['menu_items'] = []
        if 'placement_pk' in self.kwargs:
            context_data['chosen_placement'] = Placement.objects.get(pk=self.kwargs.get('placement_pk'))
        for placement in context_data['placements']:
            context_data['menu_items'].append(placement)

            placement.element.content = self.process_content(placement)

        return context_data
        