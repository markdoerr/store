# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_auto_20160413_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tag',
            field=models.ManyToManyField(related_name='tag', to='products.Tags'),
        ),
    ]
