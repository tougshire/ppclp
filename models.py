from django.db import models

class Element(models.Model):
    title = models.CharField(
            "element",
            max_length=60,
            help_text='The title of this element',
            blank=True,
        )
