from __future__ import unicode_literals
from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Categories(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'db_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    cover = ProcessedImageField(upload_to='covers', processors=[ResizeToFit(195, 243, None, '#FFFFFF')], format='JPEG', options={'quality': 100})


class Tags(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'db_tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)


class Brands(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'db_brands'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=255)


class Products(models.Model):
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'db_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-id']

    visible = models.BooleanField()
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    old_price = models.DecimalField(decimal_places=2, max_digits=7, default=True, null=True, blank=True)
    category = models.ForeignKey(Categories)
    brand = models.ForeignKey(Brands)
    tag = models.ManyToManyField(Tags, related_name='tag')
    cover = ProcessedImageField(max_length=600, upload_to='covers', processors=[ResizeToFit(195, 243, None, '#FFFFFF')], format='JPEG', options={'quality': 100})


class Images(models.Model):
    class Meta:
        db_table = 'db_images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    product = models.ForeignKey(Products)
    url = models.ImageField(upload_to='images', max_length=300)
