from ..models import Element
from django.test import TestCase
from django.apps import apps
from django.contrib import admin

class TestGeneralModelParams(TestCase):
    def setUp(self):
        pass

    def test_check_models_registered(self):
        exempted_models=[]
        for label, model in apps.all_models['ppclp'].items():
            if not model in exempted_models:
                self.assertTrue(admin.site.is_registered(model),msg=model.__name__ + ' is not registered')

    def test_check_models_str(self):
        exempted_models=[]
        for label, model in apps.all_models['ppclp'].items():
            if not model in exempted_models:
                self.assertFalse(model.__str__ == type(model).__str__, msg=model.__name__ + ' has no __str__ defined')


class ElementTestCase(TestCase):
    def setUp(self):
        Element.objects.create(title='Test element two', body='This is the second top level element', rank=2 ) 
        Element.objects.create(title='Test element one', body='This is the first top level element', rank=1 ) 
        Element.objects.create(title="Test element one alpha", body='This is the first element under element one', rank=1, parent=Element.objects.get(title='Test element one'))
        Element.objects.create(title="Test element two bravo", body='This is the second element under element two', rank=2)
        Element.objects.create(title="Test element two alpha", body='This is the first element under element two', rank=1)

