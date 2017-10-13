from django.contrib import admin

from .models import SubCategory, Category, Brand, Item
from django.contrib.humanize.templatetags.humanize import intcomma


class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_active', 'sub_category')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','get_sub_category' ,'is_active')
    exclude = ('created_on', 'updated_on')

    def get_sub_category(self, obj):
        return ",".join([str(p) for p in obj.sub_category.all()])
    
    
class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category', 'logo', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'created_on')
    search_fields = ('id', 'name',)
    
    
class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'sku', 'details', 'short_desc', 'image', 'category', 'sub_category', 'brand', 'price', 'company',
                'locations', 'active', 'stock'
              )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category', 'brand', 'edition')
    list_display = ('name', 'sku','category', 'price',  'locations', 'submitted_on', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Item, ItemAdmin)
