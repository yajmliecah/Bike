from django.contrib import admin

from bike.models import Category, Brand, Edition, Item


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class EditonAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category', 'brand', 'edition', 'price',
              'negotiable', 'condition', 'seller_type', 'fuel', 'transmission',
              'lifestyle', 'color_family', 'details'
              )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category', 'brand', 'edition')
    list_display = ('name', 'category'  , 'brand', 'edition', 'submitted_on')
    
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Edition, EditonAdmin)
admin.site.register(Item, ItemAdmin)



