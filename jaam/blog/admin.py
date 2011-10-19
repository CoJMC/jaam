from django.contrib import admin
from jaam.blog.models import BlogPost, Blog
from jaam.journalism.admin import BaseAdmin

class BlogPostAdmin(BaseAdmin):
    pass

class BlogAdmin(BaseAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blog, BlogAdmin)