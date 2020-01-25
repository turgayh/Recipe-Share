# Generated by Django 2.2.4 on 2020-01-20 18:21

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('restaurant', '0002_recipe_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingreiends',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
