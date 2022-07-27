from django.db import models

class Element(models.Model):
    body = models.TextField(
        "body",
        blank=True,
        help_text="The body (using Markdown) of the element"
    )
    is_heading = models.BooleanField(
        'is heading',
        default=0,
        help_text = 'If this is a heading or a paragraph'
    )
    rank = models.IntegerField(
        'rank',
        help_text = 'The order on the list compared to siblings'
    )
    indent = models.IntegerField(
        'indent',
        default=0,
        help_text = 'The indent level of this item'
    )