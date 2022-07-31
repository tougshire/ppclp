from django.urls import path

from . import views

app_name = 'ppclp'

urlpatterns = [
    path('page/<int:pk>', views.PageDisplay.as_view(), name='page-display'),
    path('page/<int:pk>/element/<int:element_pk>', views.PageDisplay.as_view(), name='element-display'),

]
