# Generated by Django 2.2.4 on 2020-01-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
