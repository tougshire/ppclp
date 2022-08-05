from django.db import models

class Page(models.Model):
    name = models.CharField(
        "name",
        max_length=50,
        help_text="The name of the page"
    )
    slug = models.SlugField(
        "slug",
        unique=True,
        help_text="The URL slug"
    )
    cover_photo = models.ImageField(
        "Cover Photo",
        null=True,
        blank=True,
        help_text='The cover photo for this page'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Element(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        help_text = 'The text of the headline for this elememnt'
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
        if len(self.title) > 75:
            return self.title[:70] + ' ...'
        else:
            return self.title

    class Meta:
        ordering = ['title']

class Placement(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE
    )
    element = models.ForeignKey(
        Element,
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text = 'The order in which this element appears on the page'
    )
    level = models.PositiveSmallIntegerField(
        "level",
        default=2,
        choices=((2,"h2"), (3,"h3"),(4,"h4"),(5,"h5"),(6,"h6")),
        help_text = 'The heading level of this element, corresponding to the html tags &lt;h2&gt; - &lt;h6&gt;.  Only use 2 - 6.  &lt;h1&gt; is used for the page title. '
    )
    is_hidden = models.BooleanField(
        "hidden",
        default=False,
        help_text="If this placement should not appear in the menubar or in the listing of all elements."
    )

    def __str__(self):
        element = self.element.__str__() if hasattr(self, 'element') else ''
        page = self.page.__str__() if hasattr(self,'page') else ''

        full_str = '%s on %s' % (element, page )
        if len(full_str) > 75:
            return full_str[:70] + ' ...'
        else:
            return full_str

    class Meta:
        ordering = ['page', 'order']
