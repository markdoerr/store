# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160330_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='url',
            field=models.ImageField(default=1, max_length=255, upload_to='images'),
            preserve_default=False,
        ),
    ]
