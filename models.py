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
        default=False,
        help_text = 'If this is a heading or a paragraph'
    )

    def __str__(self):
        full_name = '%s: %s' % (self.name, self.body)
        if len(full_name) > 50:
            return full_name[:45] + ' ...'
        else:
            return full_name

class Page(models.Model):
    name = models.CharField(
        "name",
        max_length=50,
        help_text="The name of the page"
    )
    slug = models.CharField(
        "slug",
        max_length=50,
        help_text="The URL slug"
    )

    def __str__(self):
        return self.name

class ElementPlacement(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE
    )
    element = models.ForeignKey(
        Element,
        on_delete=models.CASCADE
    )
    rank = models.IntegerField(
        'rank',
        help_text = 'The order on the page'
    )
    level = models.IntegerField(
        'level',
        default=0,
        help_text = 'The heading level of this placement.  Applies only to headings, not paragraphs'
    )

    def __str__(self):
        pg = self.page if hasattr(self, 'page') else "Undefined"
        el = self.element if hasattr(self, 'element') else "Undefined"
        return '%s on page %s' % (el, pg)

    class Meta:
        ordering = ['rank']