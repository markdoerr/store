# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160329_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='url',
            new_name='image',
        ),
    ]