from django.contrib import admin

from .models import Brand, Edition, Item



class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class EditonAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'image', 'category', 'brand', 'edition', 'price',
                'condition', 'details', 'locations'
              )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category', 'brand', 'edition')
    list_display = ('name', 'price', 'category'  , 'brand', 'edition',  'locations', 'submitted_on', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(Brand, BrandAdmin)
admin.site.register(Edition, EditonAdmin)
admin.site.register(Item, ItemAdmin)



