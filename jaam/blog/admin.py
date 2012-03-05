from django.contrib import admin
from django import forms
from jaam.blog.models import BlogPost, Blog
from jaam.journalism.admin import BaseAdmin
from django.contrib.auth.models import User

class BlogPostInline(admin.StackedInline):
    model = BlogPost
    extra = 1

class BlogPostAdmin(BaseAdmin):
    add_form_template = 'admin/blog_post_change.html'
    change_form_template = 'admin/blog_post_change.html'
    list_display = ('__unicode__', 'description', 'author', 'published')
    list_filter = ('blog', 'author', 'published')
    prepopulated_fields = {'slug': ('headline',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('blog', 'headline', 'slug', 'cover_photo', 'description', 'body','tags',) },),
                 ('Admin', { 'fields': ('author', 'published',) },),
                )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class BlogAdmin(BaseAdmin):
    list_display = ('__unicode__', 'subtitle', 'published')
    list_filter = ('project', 'published')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('project','title', 'slug', 'cover_photo', 'subtitle', 'description', 'tags',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blog, BlogAdmin)
