from django.contrib import admin
from jaam.videos.models import Video, VideoGallery
from jaam.journalism.admin import BaseAdmin

class VideoAdmin(BaseAdmin):
    pass

class VideoGalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)