from django.contrib import admin
from jaam.photos.models import Photo, PhotoGallery, PhotoExifData
from jaam.journalism.admin import BaseAdmin

class PhotoAdmin(BaseAdmin):
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'caption', 'journalist',)
    list_filter = ( 'project', )
    prepopulated_fields = { 'slug': ('title',)}
    fieldsets = (
                 (None, { 'fields': ('project', 'journalist', 'title', 'slug', 'image', 'caption',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
        return super(PhotoAdmin, self).get_form(request, obj, **kwargs)

class PhotoGalleryAdmin(admin.ModelAdmin):
    pass

class PhotoExifDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoExifData, PhotoExifDataAdmin)
