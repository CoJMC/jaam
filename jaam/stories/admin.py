from django.contrib import admin
from jaam.stories.models import Story

class StoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Story, StoryAdmin)