# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20160330_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='cover',
            field=models.CharField(blank=True, choices=[('True', 'cover')], max_length=255, unique=True),
        ),
    ]
