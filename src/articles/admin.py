from django.contrib import admin

from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('posted_on', 'posted_by', 'updated_on')
    

class CommentAdmin(admin.ModelAdmin):
    pass
    
class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)