from django.contrib import admin
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'image_preview', 'price', 'is_selling', 'expiration_date', 'created_at', 'updated_at') 

    # Custom method to display image preview
    def image_preview(self, obj):
        if obj.image:
            return format_html('<div style="display: flex; align-items: center;"><img src="{}" width="50" height="50" /></div>'.format(obj.image.url))
        else:
            return 'No Image'
    
    image_preview.short_description = 'Image Preview'



admin.site.register(Product, ProductAdmin)