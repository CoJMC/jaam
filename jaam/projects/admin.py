from django.contrib import admin
from jaam.projects.models import Project, ProjectLocation
from jaam.journalism.admin import BaseAdmin

class LocationInline(admin.TabularInline):
    name = "Locations"
    model = Project.locations.through
    extra = 2
    verbose_name = "Location"
    verbose_name_plural = "Locations"

class ProjectAdmin(BaseAdmin):
    change_form_template = 'admin/project_change.html'
    search_fields = ('title', 'description',)
    list_display = ('__unicode__', 'tagline', 'rss_urls', 'published', 'archived')
    exclude = [ 'locations', ]
    inlines = [ LocationInline, ]
    list_filter = ( 'locations', 'published', 'archived')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
                 (None, { 'fields': ('title', 'slug', 'tagline', 'description', 'coverGallery', 'infographic', 'tags',) },),
                 ('ProjectColors', {'fields': ('primaryColor', 'accentColor',)},),
                 ('Admin', { 'fields': ('published', 'archived') },),
                ]

class ProjectLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectLocation, ProjectLocationAdmin)
