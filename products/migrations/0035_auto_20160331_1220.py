# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20160331_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='cover',
            field=models.IntegerField(blank=True, choices=[(1, 'Cover')], default='', null=True),
        ),
    ]
