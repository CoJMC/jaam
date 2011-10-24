from django.contrib import admin
from jaam.projects.models import Project, ProjectLocation

class LocationInline(admin.TabularInline):
    name = "Locations"
    model = Project.locations.through
    extra = 2
    verbose_name = "Location"
    verbose_name_plural = "Locations"

class ProjectAdmin(admin.ModelAdmin):
    exclude = ( 'locations', )
    inlines = [ LocationInline, ]
    list_filter = ( 'locations', )

class ProjectLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectLocation, ProjectLocationAdmin)
