from django.contrib import admin

from ppclp.models import Element, ElementPlacement, Page

admin.site.register(Element)

admin.site.register(Page)

admin.site.register(ElementPlacement)
