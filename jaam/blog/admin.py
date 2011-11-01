from django.contrib import admin
from django import forms
from jaam.blog.models import BlogPost, Blog
from jaam.journalism.admin import BaseAdmin
from django.contrib.auth.models import User

class BlogPostInline(admin.StackedInline):
    model = BlogPost
    extra = 1

class BlogPostAdmin(BaseAdmin):
    list_display = ('__unicode__', 'description', 'author',)
    list_filter = ('blog','author')
    prepopulated_fields = {'slug': ('headline',)}
    fieldsets = (
                 (None, { 'fields': ('blog', 'headline', 'slug', 'description', 'body','tags',) },),
                 ('Admin', { 'fields': ('author', 'published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('author')
        return super(BlogPostAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class BlogAdmin(BaseAdmin):
    list_display = ('__unicode__', 'subtitle',)
    list_filter = ('project',)
    #inlines = [ BlogPostInline, ]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blog, BlogAdmin)
