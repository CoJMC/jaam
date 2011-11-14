from django.contrib import admin
from jaam.videos.models import Video, VideoGallery, VideoGalleryItem
from jaam.journalism.admin import BaseAdmin

class VideoAdmin(BaseAdmin):
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'caption', 'journalist',)
    list_filter = ( 'project', )
    prepopulated_fields = { 'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('project', 'journalist', 'title', 'slug', 'videoUrl', 'caption',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
        return super(VideoAdmin, self).get_form(request, obj, **kwargs)

class VideoGalleryItemInline(admin.TabularInline):
    model = VideoGalleryItem

class VideoGalleryAdmin(admin.ModelAdmin):
    inlines = [VideoGalleryItemInline]
    list_display = ('project', '__unicode__', 'introduction')
   # list_filter = ('video gallery')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
                 (None, { 'fields': ('project', 'title', 'slug', 'introduction', 'tags',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('author')
        return super(VideoGalleryAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)
