from django.contrib import admin
from jaam.blog.models import BlogPost, Blog
from jaam.journalism.admin import BaseAdmin

class BlogPostInline(admin.StackedInline):
    model = BlogPost
    extra = 1

class BlogPostAdmin(BaseAdmin):
    list_display = ('__unicode__', 'description',)
    list_filter = ('blog',)

class BlogAdmin(BaseAdmin):
    list_display = ('__unicode__', 'subtitle',)
    list_filter = ('project',)
    inlines = [ BlogPostInline, ]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blog, BlogAdmin)
