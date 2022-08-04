from django.urls import path

from . import views

app_name = 'ppclp'

urlpatterns = [
    path('page/<int:pk>', views.PageDisplay.as_view(), name='page-display'),
    path('page/<int:pk>/placement/<int:placement_pk>', views.PageDisplay.as_view(), name='placement-display'),
    path('page/<int:pk>/edit', views.PageUpdate.as_view(), name='page-update'),

]
