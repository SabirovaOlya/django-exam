from django.contrib import admin
from .models import Product, ProductImage, ProductVideo


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 3
    min_num = 0


class ProductVideoStackedInline(admin.StackedInline):
    model = ProductVideo
    extra = 1
    min_num = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'is_premium', )
    list_display_links = ('id', 'name', )
    list_filter = ('name', 'is_premium')
    inlines = (ProductImageStackedInline, )

