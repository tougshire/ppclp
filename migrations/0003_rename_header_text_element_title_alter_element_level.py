# Generated by Django 4.0.5 on 2022-07-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppclp', '0002_element_date_modified_alter_element_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='header_text',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='element',
            name='level',
            field=models.PositiveSmallIntegerField(default=2, help_text='The heading level of this element, corresponding to the html tags <h2> - <h6>.  Note: The default is 2. <h1> is used for the page title', verbose_name='level'),
        ),
    ]
