# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 05:51
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_auto_20160413_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(max_length=500, upload_to='covers'),
        ),
    ]
