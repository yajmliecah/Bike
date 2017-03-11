from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'location', 'avatar', 'mobile_number')
    list_display = ('user', 'membership', 'mobile_number')
    search_fields = ('user',)
    
admin.site.register(Profile, ProfileAdmin)
    
    