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
    search_fields = ('title', 'description',)
    list_display = ('__unicode__', 'tagline', 'rss_urls', 'published')
    exclude = [ 'locations', ]
    inlines = [ LocationInline, ]
    list_filter = ( 'locations', 'published')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
                 (None, { 'fields': ('title', 'slug', 'tagline', 'description', 'coverGallery', 'tags',) },),
                 ('ProjectColors', {'fields': ('primaryColor', 'accentColor',)},),
                 ('Admin', { 'fields': ('published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
        return super(ProjectAdmin, self).get_form(request, obj, **kwargs)

class ProjectLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectLocation, ProjectLocationAdmin)
