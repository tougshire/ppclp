from django.contrib import admin
from ppclp.models import Element, Page, Placement

admin.site.register(Element)

admin.site.register(Page)

class PlacementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'level']
    list_editable = ['order', 'level']

admin.site.register(Placement, PlacementAdmin)
