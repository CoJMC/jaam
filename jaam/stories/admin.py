from django.contrib import admin
from jaam.stories.models import Story
from jaam.journalism.admin import BaseAdmin

class StoryAdmin(BaseAdmin):
    pass

admin.site.register(Story, StoryAdmin)