from tkinter import W
from ..models import Page,Element
from ..views import PageDetail
from django.test import TestCase
from django.apps import apps
from django.contrib import admin


class TestContentConversion(TestCase):
    def setUp(self):
        self.page_one = Page.objects.create(name='First Page')
        self.element_one =Element.objects.create(page=self.page_one, header_text="Element One", level=0, content="# this should be h2 # \n\n plain ***em***")
        self.element_two =Element.objects.create(page=self.page_one, header_text="Element Two", level=1, content="# this should be h3 # \n\n plain ***em***")
        self.element_three =Element.objects.create(page=self.page_one, header_text="Element Three", level=0, content="## this should be h3 ## \n\n plain ***em***")
        self.element_four =Element.objects.create(page=self.page_one, header_text="Element Four", level=3, content="## this should be h6 ## \n\n plain ***em***")
        self.element_five =Element.objects.create(page=self.page_one, header_text="Element Five", level=3, content="### this should be h6 class h7 ### \n\n plain ***em***")
        self.element_six =Element.objects.create(page=self.page_one, header_text="Element Five", level=4, content="## this should be h6 class h7 ## \n\n plain ***em***")
        self.element_seven =Element.objects.create(page=self.page_one, header_text="Element Five", level=4, content="## this should be h6 class h7 ## \n\n plain ***em***")
 

    def test_check_markdown(self):
        view = PageDetail(object=self.page_one)
        print('tp227tl12', view.get_context_data()['elements'])
        