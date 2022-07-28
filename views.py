from django import views
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Page


class PageDetail(DetailView):
    model = Page
    template_name = 'ppclp/page_detail.html'