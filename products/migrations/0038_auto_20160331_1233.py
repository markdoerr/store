# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20160331_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='cover',
        ),
        migrations.AddField(
            model_name='products',
            name='cover',
            field=models.ImageField(default=1, max_length=300, upload_to='covers'),
            preserve_default=False,
        ),
    ]
