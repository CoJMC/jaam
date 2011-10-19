from django.contrib import admin
from jaam.projects.models import Project, ProjectLocation

class ProjectAdmin(admin.ModelAdmin):
    pass

class ProjectLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectLocation, ProjectLocationAdmin)