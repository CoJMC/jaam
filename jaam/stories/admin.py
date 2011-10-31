from django.contrib import admin
from jaam.stories.models import Story
from jaam.journalism.admin import BaseAdmin

class StoryAdmin(BaseAdmin):
    fieldsets = (
        (None, { 'fields':
            ('project', 'author', 'headline', 'blurb', 'body') }),
        ('Admin', { 'fields':
            ('published',) }),
    )
    pass

admin.site.register(Story, StoryAdmin)
