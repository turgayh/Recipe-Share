# Generated by Django 3.0.2 on 2020-01-25 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_recipe_ingreiends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingreiends',
        ),
    ]