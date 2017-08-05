from django.contrib import admin

from .models import Category, Brand, Edition, Item
from django.contrib.humanize.templatetags.humanize import intcomma


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category', 'logo', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'created_on')
    search_fields = ('id', 'name',)


class EditionAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'brand')
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'image', 'category', 'brand', 'edition', 'price', 'company',
                'condition', 'details', 'locations', 'active'
              )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category', 'brand', 'edition')
    list_display = ('name', 'price',  'locations', 'submitted_on', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Item, ItemAdmin)
