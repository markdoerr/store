# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_remove_images_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='cover',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
