# Generated by Django 4.1 on 2022-08-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppclp', '0007_alter_placement_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='The URL slug', verbose_name='slug'),
        ),
    ]
