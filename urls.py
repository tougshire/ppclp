from django.urls import path

from . import views

app_name = 'ppclp'

urlpatterns = [
    path('morgan/', views.morgan),
]
