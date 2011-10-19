from django.contrib import admin
from jaam.blog.models import BlogPost, Blog

class BlogPostAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blog, BlogAdmin)