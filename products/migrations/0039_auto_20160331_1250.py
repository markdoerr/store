# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:50
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20160331_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(upload_to='covers'),
        ),
    ]
