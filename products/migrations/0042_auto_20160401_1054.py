# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_auto_20160401_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.FloatField(null=True),
        ),
    ]