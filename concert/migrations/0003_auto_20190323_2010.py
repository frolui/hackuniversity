# Generated by Django 2.1.5 on 2019-03-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0002_sounds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ivents',
            name='image',
        ),
        migrations.RemoveField(
            model_name='person',
            name='picture',
        ),
    ]
