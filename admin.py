from django.contrib import admin

from ppclp.models import Element, Page

class ElementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order']
    list_editable = ['order']

admin.site.register(Element, ElementAdmin)

admin.site.register(Page)

