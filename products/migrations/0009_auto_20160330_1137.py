# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_images_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='cover',
            field=models.IntegerField(choices=[('cover', 1), ('non-cover', '')]),
        ),
    ]
