from django.contrib import admin

from .models import SubCategory, Category, Brand, Item
from django.contrib.humanize.templatetags.humanize import intcomma


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ('name', 'sku', 'category', 'sub_category', 'brand', 'price', 'stock', 'active')


class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    inlines = [ItemInline,]


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_active', 'sub_categories')
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('created_on', 'updated_on')
    list_display = ('name', 'get_sub_category')
    inlines = [ItemInline,]

    def get_sub_category(self, obj):
        return ", ".join([str(p) for p in obj.sub_categories.all()])


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
    list_display = ('name', 'sku', 'category', 'brand', 'price', 'stock', 'active', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Item, ItemAdmin)
