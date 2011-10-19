from django.contrib import admin
from jaam.videos.models import Video, VideoGallery

class VideoAdmin(admin.ModelAdmin):
    pass

class VideoGalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)