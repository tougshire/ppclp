from tkinter import W
from ..models import Page,Element, Placement
from ..views import PageDisplay
from django.test import TestCase
from django.apps import apps
from django.contrib import admin


class TestPageDetailView(TestCase):
    def setUp(self):
        self.page_one = Page.objects.create(name='First Page')
 

    def test_check_markdown(self):
        view = PageDisplay(object=self.page_one, kwargs={})

        element_one =Element.objects.create(title="Element One", content="# this should be h3 \n\n plain ***em***")
        element_two =Element.objects.create(title="Element Two", content="# this should be h4 \n\n plain ***em***")
        element_three =Element.objects.create(title="Element Three", content="## this should be h4 \n\n plain ***em***")
        element_four =Element.objects.create(title="Element Four", content="## this should be h6 \n\n plain ***em***")
        element_five =Element.objects.create(title="Element Five", content="### this should be h6 class h7  \n\n plain ***em***")
        element_six =Element.objects.create(title="Element Five", content="## this should be h6 class h7 \n\n plain ***em***")
 
        placement_one = Placement.objects.create(page=self.page_one, element=element_one)
        placement_two = Placement.objects.create(page=self.page_one, element=element_two, order=1, level=3)
        placement_three = Placement.objects.create(page=self.page_one, element=element_three, order=2, level=2)
        placement_four = Placement.objects.create(page=self.page_one, element=element_four, order=3, level=4)
        placement_five = Placement.objects.create(page=self.page_one, element=element_five, order=4, level=4)
        placement_six = Placement.objects.create(page=self.page_one, element=element_six, order=5, level=5)

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

    def test_check_hidden_placements(self):
        test_element_hid = Element.objects.create(title="Hidden", content="This is the hidden test element")        
        test_element_one = Element.objects.create(title="One", content="This is test element one")
        test_element_two = Element.objects.create(title="Two", content="This is test element two")
        test_element_three = Element.objects.create(title="Three", content="This is test element three")

        placement_one = Placement.objects.create(page=self.page_one, element=test_element_one, order=2, level=2 )
        placement_hid = Placement.objects.create(page=self.page_one, element=test_element_hid, order=3, level=1 )
        placement_two = Placement.objects.create(page=self.page_one, element=test_element_two, order=4, level=2 )
        placement_three = Placement.objects.create(page=self.page_one, element=test_element_three, order=5, level=2 )

#        view = PageDisplay(object=self.page_one, kwargs={})
#        view.as_view(placement_pk=2)
        dir(PageDisplay)
        view = PageDisplay.as_view(kwargs={'object':self.page_one})

        print('tp2281i43', view.get_context_data()['placements'])
        print('tp2282547', [placement.element.content for placement in view.get_context_data()['placements']])
