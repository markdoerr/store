# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20160330_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='cover',
            field=models.IntegerField(blank=True, choices=[(1, 'Make cover')], null=True, unique=True),
        ),
    ]
