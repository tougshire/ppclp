from django.urls import path

from . import views

app_name = 'ppclp'

urlpatterns = [
    path('page/<int:pk>', views.PageDetail.as_view(), name='page-detail'),
]
