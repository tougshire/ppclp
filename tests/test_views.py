from tkinter import W
from ..models import Page,Element
from ..views import PageDetail
from django.test import TestCase
from django.apps import apps
from django.contrib import admin


class TestContentConversion(TestCase):
    def setUp(self):
        self.page_one = Page.objects.create(name='First Page')
        self.element_one =Element.objects.create(page=self.page_one, title="Element One", level=2, content="# this should h3 \n\n plain ***em***")
        self.element_two =Element.objects.create(page=self.page_one, title="Element Two", level=3, content="# this should be h4 \n\n plain ***em***")
        self.element_three =Element.objects.create(page=self.page_one, title="Element Three", level=2, content="## this should be h4 \n\n plain ***em***")
        self.element_four =Element.objects.create(page=self.page_one, title="Element Four", level=4, content="## this should be h6 \n\n plain ***em***")
        self.element_five =Element.objects.create(page=self.page_one, title="Element Five", level=4, content="### this should be h6 class h7  \n\n plain ***em***")
        self.element_six =Element.objects.create(page=self.page_one, title="Element Five", level=5, content="## this should be h6 class h7 \n\n plain ***em***")
 

    def test_check_markdown(self):
        view = PageDetail(object=self.page_one)
        print('tp227tl12', view.get_context_data()['elements'])
        print('tp227u701', view.get_context_data()['elements'].get(title="Element One").content)        
        print('tp227u702', view.get_context_data()['elements'].get(title="Element Two").content)        