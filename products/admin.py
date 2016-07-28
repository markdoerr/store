from django.contrib import admin
from .models import Products, Categories, Tags, Images, Brands

from django.core.urlresolvers import reverse


class ImageInLIne(admin.StackedInline):
    model = Images


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInLIne]
    save_on_top = True
    list_display = ['title', 'brand', 'visible', 'old_price']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', )
    list_filter = ('category', )
    ordering = ('-id', )
    filter_horizontal = ['tag']
    radio_fields = {'category': admin.HORIZONTAL, 'brand': admin.HORIZONTAL}
    view_on_site = True

    def view_on_site(self, obj):
        return reverse('product_view', kwargs={'category': obj.category.slug, 'slug': obj.slug})


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tags)
admin.site.register(Brands)
