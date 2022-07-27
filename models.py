from django.db import models

class Element(models.Model):
    name = models.CharField(
        "name",
        max_length=50,
        help_text="The name - seen only by administrators"
    )
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

    def __str__(self):
        full_name = '%s: %s' % (self.name, self.body)
        if full_name > 50:
            return full_name[:45] + ' ...'
        else:
            return full_name

        