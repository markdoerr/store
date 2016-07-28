# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_auto_20160419_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
