# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20160331_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='cover',
            field=models.IntegerField(blank=True, choices=[('1', 'Cover')], default='', null=True),
        ),
    ]
