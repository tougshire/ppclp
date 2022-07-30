from django.db import models


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

class Element(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        "name",
        max_length=100,
        blank=True,
        help_text = 'The name of the element, seen only by editors'
    )
    header_text = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text = 'The text of the headline for this elememnt'
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text = 'The order in which this element appears on the page'
    )
    level = models.PositiveSmallIntegerField(
        "level",
        default=2,
        help_text = 'The heading level of this element, corresponding to the html tags <h2> - <h6>.  Note: The default is 2. <h1> is used for the page title'
    )
    content = models.TextField(
        "content",
        blank=True,
        help_text='The content of the block'
    )
    date_modified = models.DateField(
        auto_now=True,
        help_text='The date of last modification'
    )

    def __str__(self):
        full_name = '%s: %s' % (self.name, self.content)
        if len(full_name) > 75:
            return full_name[:70] + ' ...'
        else:
            return full_name

    class Meta:
        ordering = ['page', 'order', 'level', 'name']

    