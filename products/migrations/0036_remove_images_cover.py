# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20160331_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='cover',
        ),
    ]
