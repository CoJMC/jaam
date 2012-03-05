from django.contrib import admin
from jaam.stories.models import Story
from jaam.journalism.admin import BaseAdmin

class StoryAdmin(BaseAdmin):
    list_display = ('__unicode__', 'blurb', 'author', 'published')
    list_filter = ('author', 'published')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, { 'fields':
            ('project', 'title', 'slug', 'blurb', 'body', 'tags') }),
        ('Admin', { 'fields':
            ('published', 'author') }),
    )
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('author')
        return super(StoryAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Story, StoryAdmin)
