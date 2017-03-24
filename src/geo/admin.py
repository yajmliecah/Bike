from django.contrib import admin

from .models import Country, City


class CountryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    

class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'country')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'country')
    
    
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)