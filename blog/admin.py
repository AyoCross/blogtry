from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','timeregis',)
    search_fields = ('title',)

admin.site.register(BlogPost,BlogPostAdmin)
