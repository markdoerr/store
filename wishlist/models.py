from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from products.models import Products


class Wishlist(models.Model):
    def __repr__(self):
        return self.user

    class Meta:
        db_table = 'db_wishlist'
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlist'
        # add ordering for new products
        #ordering = ['id']

    user = models.OneToOneField(User)
    product = models.ManyToManyField(Products)
