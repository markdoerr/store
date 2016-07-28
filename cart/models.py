from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from products.models import Products
from django.core.exceptions import ValidationError


class Cart(models.Model):
    def __repr__(self):
        return self.product

    class Meta:
        db_table = 'db_cart'
        verbose_name = 'cart'
        verbose_name_plural = 'cart'
        unique_together = ("user", "product")
        ordering = ['-id']

    #validation in django administration
    def validate_quantity(value):
        if value == 0 or value > 999:
            raise ValidationError('%s - is incorrect number, 1-999 only!' % value)

    user = models.ForeignKey(User)
    quantity = models.PositiveIntegerField(validators=[validate_quantity], default=1)
    product = models.ForeignKey(Products)

    @property
    def total_item_cost(self):
        return self.quantity * self.product.price
