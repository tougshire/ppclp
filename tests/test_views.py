from tkinter import W
from ..models import Page,Element, Placement
from ..views import PageDisplay
from django.test import TestCase
from django.apps import apps
from django.contrib import admin


class TestPageDetailView(TestCase):
    def setUp(self):
        self.page_one = Page.objects.create(name='First Page')
 
        self.element_one =Element.objects.create(title="Element One", content="# this should be h3 \n\n plain ***em***")
        self.element_two =Element.objects.create(title="Element Two", content="# this should be h4 \n\n plain ***em***")
        self.element_three =Element.objects.create(title="Element Three", content="## this should be h4 \n\n plain ***em***")
        self.element_four =Element.objects.create(title="Element Four", content="## this should be h6 \n\n plain ***em***")
        self.element_five =Element.objects.create(title="Element Five", content="### this should be h6 class h7  \n\n plain ***em***")
        self.element_six =Element.objects.create(title="Element Five", content="## this should be h6 class h7 \n\n plain ***em***")
 
        self.placement_one = Placement.objects.create(page=self.page_one, element=self.element_one)
        self.placement_two = Placement.objects.create(page=self.page_one, element=self.element_two, order=1, level=3)
        self.placement_three = Placement.objects.create(page=self.page_one, element=self.element_three, order=2, level=2)
        self.placement_four = Placement.objects.create(page=self.page_one, element=self.element_four, order=3, level=4)
        self.placement_five = Placement.objects.create(page=self.page_one, element=self.element_five, order=4, level=4)
        self.placement_six = Placement.objects.create(page=self.page_one, element=self.element_six, order=5, level=5)

    def test_check_markdown(self):
        view = PageDisplay(object=self.page_one, kwargs={})
        placements = view.get_context_data()['placements']
        test_string_prefix='<div class="content-block"></div>'
        test_string=test_string_prefix + '<h3>this should be h3</h3>'
        self.assertEqual(placements[0].element.content[:len(test_string)],test_string)
        test_string=test_string_prefix + '<h4>this should be h4</h4>'
        self.assertEqual(placements[1].element.content[:len(test_string)],test_string)
        test_string=test_string_prefix + '<h4>this should be h4</h4>'
        self.assertEqual(placements[2].element.content[:len(test_string)],test_string)
        test_string=test_string_prefix + '<h6>this should be h6</h6>'
        self.assertEqual(placements[3].element.content[:len(test_string)],test_string)
        test_string=test_string_prefix + '<h6 class="h7">this should be h6 class h7</h6>'
        self.assertEqual(placements[4].element.content[:len(test_string)],test_string)
        test_string=test_string_prefix + '<h6 class="h7">this should be h6 class h7</h6>'
        self.assertEqual(placements[5].element.content[:len(test_string)],test_string)

