from django.contrib import admin
from jaam.stories.models import Story
from jaam.journalism.admin import BaseAdmin

class StoryAdmin(BaseAdmin):
    add_form_template = 'admin/story_change.html'
    change_form_template = 'admin/story_change.html'
    list_display = ('__unicode__', 'project', 'blurb', 'author', 'published')
    list_filter = ('project', 'author', 'published')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, { 'fields':
            ('project', 'title', 'slug', 'blurb', 'cover_photo', 'body', 'tags') }),
        ('Admin', { 'fields':
            ('author', 'published') }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Story, StoryAdmin)
