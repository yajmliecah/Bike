from django.contrib import admin

from .models import Country, Region


class CountryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    

class RegionAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'country')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'country')
    
    
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)