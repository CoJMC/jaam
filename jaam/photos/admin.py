from django.contrib import admin
from jaam.photos.models import Photo, PhotoGallery, PhotoExifData
from jaam.journalism.admin import BaseAdmin

class PhotoAdmin(BaseAdmin):
    pass

class PhotoGalleryAdmin(admin.ModelAdmin):
    pass

class PhotoExifDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoExifData, PhotoExifDataAdmin)